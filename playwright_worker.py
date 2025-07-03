import os
from playwright.async_api import async_playwright

async def run_playwright(url: str, out_dir: str = "results/temp"):
    os.makedirs(out_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context()
        page = await context.new_page()

        print(f"👉 Navigating to: {url}")
        await page.goto(url, wait_until="networkidle")
        await page.add_style_tag(content="""
          * {
            transition: none !important;
            animation: none !important;
          }
        """)

        # 1) 截放大前的页面
        before_path = os.path.join(out_dir, "before.png")
        await page.screenshot(path=before_path, full_page=False)
        print(f"✅ Screenshot saved: {before_path}")

        # 2) 放大到 200%（使用 body.zoom）
        await page.evaluate("""
            document.body.style.zoom = '200%';
            window.dispatchEvent(new Event('resize'));
        """)

        await page.wait_for_timeout(3000)  # 等待渲染

        # 3) 截放大后的页面
        after_path = os.path.join(out_dir, "after.png")
        await page.screenshot(path=after_path, full_page=False)
        print(f"✅ Screenshot saved: {after_path}")

        await browser.close()
