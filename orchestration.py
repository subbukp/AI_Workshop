from pydantic_ai import Agent
from openai import AsyncOpenAI
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.settings import ModelSettings
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def call_llm(system_prompt, user_prompt):
    """Call LLM with the given prompts."""
    portkey_client = AsyncOpenAI(
        api_key=os.getenv('portkey_token'),
        base_url="https://api.portkey.ai/v1"
    )

    agent = Agent(
        model = OpenAIChatModel(
            model_name="@openrouter-09cb28/google/gemini-2.5-flash",
            provider=OpenAIProvider(openai_client=portkey_client)
        ),
        system_prompt=system_prompt,
        output_type=str,
        model_settings=ModelSettings(
            temperature=0.1,
            max_tokens=4096,
            top_p=0.9
        )
    )
    res = None
    try:
        response = await agent.run(user_prompt)
        res = response.output
    except Exception as e:
        print(f"LLM error: {str(e)}")
    return res

async def main():
    
    res = await call_llm("You are a helpful assistant.",
        "What is Portkey?")
    print(res)
    
asyncio.run(main())