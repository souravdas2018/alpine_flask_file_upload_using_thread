import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')  # Load from environment variable

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a small essay on cow"}
    ]
)

# Extract and print the AI's reply cleanly
answer = response['choices'][0]['message']['content']
print("\n=== AI Response ===")
print(answer)
print("===================")