from openai import AsyncOpenAI

from config import OPENAI_API_KEY

from promt import SYSTEM_PROMPT

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


async def generate_text(prompt):

    response = await client.responses.create(
        model="gpt-5",
        instructions=SYSTEM_PROMPT,
        input=prompt
    )

    return response.output_text

    return response.output_text