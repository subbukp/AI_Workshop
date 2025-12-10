from portkey_ai import Portkey
import os 
from dotenv import load_dotenv

load_dotenv() 

'''with open(".env") as f:
    for line in f:
        key,value = line.strip().split("=",1)
        os.environ[key]=value'''
        
portkey_api_key = os.getenv('portkey_token')
provider_name = "openrouter-09cb28"
portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)


response = portkey_client.chat.completions.create(
    model="google/gemini-2.5-flash", messages=[{"role": "user", "content": "Testing 12,..."}], cache=False
)
print(response.choices[0].message.content)