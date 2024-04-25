from openai import OpenAI
from backend import history, prompt_config
from backend.rag import rag_results
import json, datetime

llm = OpenAI()

MODEL = "gpt-4-turbo"

def generated_suggested_responses(conversation_id):
    prompt_stack = [
        {"role": "system", "content": prompt_config.generate_suggestions_prompt},
        *history.database[conversation_id]
    ]

    completion = llm.chat.completions.create(
        model=MODEL,
        messages=prompt_stack
    )

    content = completion.choices[0].message.content
    try:
        suggested_responses = json.loads(content)
    except json.JSONDecodeError:
        print(content)
        return []

    return suggested_responses

def get_context():
    current_datetime = datetime.datetime.now()
    date_string = current_datetime.strftime('It is currently %A, %B %d %Y. The time of day is %H:%M:%S.')
    return date_string + prompt_config.context_prompt

def invoke(user_input, conversation_id):
    docs, sources = rag_results(user_input, conversation_id)
    
    prompt_stack = [
        {"role": "system", "content": prompt_config.system_prompt},
        {"role": "system", "content": get_context()},
        {"role": "system", "content": docs},
        *history.database[conversation_id],
        {"role": "user", "content": user_input}
    ]

    print("PROMPT STACK")
    print("RAG:")
    print(docs)
    print()
    print("HISTORY:")
    for message in history.database[conversation_id]:
        print(message["role"] + ": " + message["content"])
    print()
    print("USER INPUT:")
    print(user_input)
    print()
    print()

    completion = llm.chat.completions.create(
        model=MODEL,
        messages=prompt_stack
    )

    content = completion.choices[0].message.content

    print("RESPONSE:")
    print(content)

    return content, sources