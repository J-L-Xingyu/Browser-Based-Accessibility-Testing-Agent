from google import genai
from google.genai import types
import prompt
from dotenv import load_dotenv
import os
import json
import re

def analyze_screenshot(image_path):
    # 加载 .env 文件
    load_dotenv()

    # 从环境变量里拿到
    google_api_key = os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=google_api_key)
    # Upload the first image
    image1_path = f"{image_path}/before.png"
    uploaded_file = client.files.upload(file=image1_path)

    # Prepare the second image as inline data
    image2_path = f"{image_path}/after.png"
    with open(image2_path, 'rb') as f:
        img2_bytes = f.read()

    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=[
            prompt.a11y_AGENT_INSTR,
            uploaded_file,  # Use the uploaded file reference
            types.Part.from_bytes(
                data=img2_bytes,
                mime_type='image/png'
            )
        ]
    )

    # ✅ 打印原始输出，调试时留着
    # print("🔍 Raw response text:", response.text)

    try:
        # 用正则只提取最外层 {...}
        match = re.search(r'\{[\s\S]*\}', response.text)
        if match:
            cleaned = match.group(0)
            print("✅ Cleaned JSON candidate:", cleaned)
            result_json = json.loads(cleaned)
        else:
            raise ValueError("No JSON found in output.")
    except Exception as e:
        print(f"❌ Could not parse JSON! Reason: {e}")
        result_json = {
            "issues": [],
            "raw_output": response.text
        }

    # print("✅ Parsed result_json:", result_json)

    return result_json

