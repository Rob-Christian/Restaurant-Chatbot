from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(message):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message.content