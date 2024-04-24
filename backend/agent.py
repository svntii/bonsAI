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
    try:
        suggested_responses = json.loads(content)
    except json.JSONDecodeError:
        print(content)
        return []

    return suggested_responses

def invoke(user_input, conversation_id):
    docs, sources = rag_results(user_input, conversation_id)
    
    prompt_stack = [
        {"role": "system", "content": prompt_config.system_prompt},
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
        model="gpt-3.5-turbo",
        messages=prompt_stack
    )

    content = completion.choices[0].message.content

    print("RESPONSE:")
    print(content)

    return content, sources