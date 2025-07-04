
# 🧪 Browser-Based Accessibility Testing Agent

This project is an **automated accessibility testing agent** focused on **WCAG 2.2 SC 1.4.4 (Resize Text)**.  
It helps you test whether your web pages maintain **content and functionality** when text is resized up to 200% — an essential requirement for users with low vision.

---

## 🔍 How It Works

The workflow for each target URL:
1. **Open page with Playwright**  
2. **Apply CSS transformations** to simulate 200% text size  
3. **Take before & after screenshots**
4. **Send `before.png`, `after.png` to a Vision-LM** (like Gemini) with a carefully crafted prompt
5. **Parse structured JSON** output from the model
6. **Generate a Markdown report**, including:
   - Test summary
   - Screenshot comparison
   - Detailed issue breakdown
   - Raw model output for traceability

---

## ⚙️ Project Structure

```plaintext
.
├── results/
│   ├── example-com/
│   │   ├── report.md
│   │   ├── before.png
│   │   ├── after.png
│   ├── testsite-org-page/
│   │   ├── report.md
│   │   ├── before.png
│   │   ├── after.png
├── test/
│   ├── urls.txt             # list of target URLs
├── report_generator.py
├── run_agent.py  
├── prompt.py  
├── vision_analyzer.py  
├── .env                     # contains your GEMINI API key etc.
```

---

## 🚀 Installation

### 1️⃣ Install Python Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Your `requirements.txt` should include:

```plaintext
playwright
python-dotenv
python-slugify
google-genai  # or your specific Gemini SDK
```

---

### 2️⃣ Install Playwright Browsers

```bash
playwright install
```

---

### 3️⃣ Setup `.env`

Create a `.env` file with your Gemini API key:

```env
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

---

## 🏃 Usage

### ✅ Single URL Test

```bash
python run_agent.py --url https://example.com
```

This will:
- Generate `before.png` & `after.png`
- Produce `report.md`

---

### ✅ Batch Mode (Multiple URLs)

Rewrite `test/urls.txt`:

```plaintext
https://example.com
https://google.com
```

Run:

```bash
python run_agent.py --urls-file test/urls.txt  
```

Each site gets its own:
- `results/<slug>-before.png`
- `results/<slug>-after.png`
- `results/<slug>/report.md`

---

## 📑 Report Structure

Each Markdown report includes:
- 📝 **Summary** at the top: Status, issue count by type
- 📸 **Before & After Screenshots**
- 🗂️ **Detailed issue breakdown** (with type, description, suggestion)
- 🗄️ **Raw JSON output** (for traceability & debugging)

✅ **Example Summary**

```markdown
## ✅ Summary

- Status: ❌ Issues found
- Total issues: 2
  - ContentLoss: 0
  - HorizontalScroll: 1
  - OverlappingElements: 1
```
