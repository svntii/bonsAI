from openai import OpenAI
from backend import history, prompt_config

llm = OpenAI()

def invoke(user_input, conversation_id):
    prompt_stack = [
        {"role": "system", "content": prompt_config.system_prompt},
        *history.database[conversation_id],
        {"role": "user", "content": user_input}
    ]

    completion = llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt_stack
    )

    print(prompt_stack)

    return completion.choices[0].message.content