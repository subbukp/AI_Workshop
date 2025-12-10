from portkey_ai import Portkey
import os 
from dotenv import load_dotenv
load_dotenv()

portkey_api_key = os.getenv('portkey_token')
provider_name = "openrouter-09cb28"
portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)

message = [{"role": "system", "content": """
You are a helpful assistant. and your name is karan"
"""}]
while True:
    message.append({"role":"user", "content": input("user:")})
    response = portkey_client.chat.completions.create(
        model="google/gemini-2.5-flash", messages=message, cache=False
    )
    #message.append({"role":"assistant", "content":response.choices[0].message.content})
    print(response.choices[0].message.content)
    message = [{"role": "system", "content": """
You are a helpful assistant. and your name is karan"
"""}]
    print("="*100)
    
    
#print(response.choices[0].message.content)