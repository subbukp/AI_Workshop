from portkey_ai import Portkey

portkey = Portkey(
  api_key = "/sAy/+AurtlD9d9TtQf/HxYtXWJa"
)

response = portkey.chat.completions.create(
    model = "@google-0aed74/gemini-2.5-flash",
    messages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is Portkey"}
    ],
    MAX_TOKENS = 512
)

print(response.choices[0].message.content)