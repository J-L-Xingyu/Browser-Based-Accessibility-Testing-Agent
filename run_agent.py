import asyncio
import argparse
import os
from playwright_worker import run_playwright
from vision_analyzer import analyze_screenshot
from report_generator import save_report
from urllib.parse import urlparse
from slugify import slugify  # pip install python-slugify

def slugify_url(url):
    parsed = urlparse(url)
    return slugify(parsed.netloc + parsed.path.replace("/", "-"))

def run_one_url(url):
    slug = slugify_url(url)
    out_dir = os.path.join("results", slug)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n🚀 Running accessibility agent for: {url} -> {out_dir}")

    # 1) Playwright 打开网页并生成截图
    asyncio.run(run_playwright(url, out_dir=out_dir))

    # 2) Vision-LM 分析放大后截图
    result_json = analyze_screenshot(os.path.join(out_dir))

    # 3) 保存报告
    save_report(result_json, url, out_dir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="A single URL to test")
    parser.add_argument("--urls-file", help="Path to file with URLs (one per line)")
    args = parser.parse_args()

    if args.url and args.urls_file:
        raise ValueError("❌ You can only specify either --url OR --urls-file, not both!")

    if not args.url and not args.urls_file:
        raise ValueError("❌ You must specify either --url OR --urls-file!")

    if args.url:
        run_one_url(args.url)
    else:
        with open(args.urls_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
        for url in urls:
            run_one_url(url)

if __name__ == "__main__":
    main()
