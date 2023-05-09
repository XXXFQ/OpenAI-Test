import openai
import os
from dotenv import load_dotenv

# 環境変数へ反映
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        { "role": "system", "content": "原神はどんなゲーム?" },
    ]
)
print(response.choices[0]["message"]["content"])