import os
import json
from datetime import datetime
from collections import Counter

def save_report(data, url, out_dir="results/temp"):
    os.makedirs("results_only_after", exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resize_percent = 200

    issues = data.get("issues", [])
    total_issues = len(issues)
    type_counts = Counter([i["type"] for i in issues])

    md = []

    # === 报告头部 ===
    md.append("# Accessibility Report\n")
    md.append(f"**URL tested**: {url}  ")
    md.append(f"**Resize Percent**: {resize_percent}%  ")
    md.append(f"**WCAG SC**: 1.4.4 Resize Text  ")
    md.append(f"**Generated At**: {now}\n")

    md.append(f"---\n")

    # === 结论 Summary ===
    md.append("## ✅ Summary\n")
    if total_issues > 0:
        md.append(f"- **Status**: ❌ Issues found")
    else:
        md.append(f"- **Status**: ✅ No issues found 🎉")

    md.append(f"- **Total issues**: {total_issues}")
    for t in ["ContentLoss", "HorizontalScroll", "OverlappingElements"]:
        md.append(f"  - {t}: {type_counts.get(t, 0)}")

    md.append("\n---\n")

    # === 截图 ===
    md.append("## 📸 Screenshots\n")
    md.append("| Before Resize | After Resize |")
    md.append("| -------------- | ------------- |")
    md.append("| ![Before](before.png) | ![After](after.png) |")

    md.append("\n---\n")

    # === Issues 详情 ===
    md.append("## 🗂️ Issues Details\n")

    if total_issues > 0:
        for idx, issue in enumerate(issues, 1):
            md.append(f"### {idx}️⃣ Type: {issue['type']}\n")
            desc = issue["description"].strip().replace("\n", " ")
            sugg = issue["suggestion"].strip().replace("\n", " ")
            md.append(f"**Description:**  \n{desc}\n")
            md.append(f"**Suggestion:**  \n{sugg}\n")
            md.append("\n---\n")
    else:
        md.append("_No issues found!_ 🎉\n")

    # === 原始 JSON 输出 ===
    md.append("\n## 🗄️ Raw Model Output\n")
    md.append("<details>\n<summary>Click to expand raw JSON output</summary>\n\n")
    md.append(f"```json\n{json.dumps(data, indent=2)}\n```")
    md.append("\n</details>\n")

    # 保存文件
    report_filename = os.path.join(out_dir, "report.md")
    with open(report_filename, "w") as f:
        f.write("\n".join(md))

    print(f"📑 Markdown report saved to {report_filename}")
