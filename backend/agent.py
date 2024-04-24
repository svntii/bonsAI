from openai import OpenAI
from backend import history, prompt_config
from backend.rag import rag_results
import json

llm = OpenAI()

def generated_suggested_responses(conversation_id):
    prompt_stack = [
        {"role": "system", "content": prompt_config.generate_suggestions_prompt},
        *history.database[conversation_id]
    ]

    completion = llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt_stack
    )

    content = completion.choices[0].message.content
    suggested_responses = json.loads(content)

    return suggested_responses

def invoke(user_input, conversation_id):
    docs, sources = rag_results(user_input, conversation_id)
    prompt_stack = [
        {"role": "system", "content": prompt_config.system_prompt},
        {"role": "system", "content": docs},
        *history.database[conversation_id],
        {"role": "user", "content": user_input}
    ]

    completion = llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt_stack
    )

    print(prompt_stack)

    return completion.choices[0].message.content