from openai import AsyncOpenAI

from config import OPENAI_API_KEY

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


async def generate_text(prompt: str):

    response = await client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text