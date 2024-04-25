from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from backend import history, prompt_config
from langchain_pinecone import PineconeVectorStore
import os
import json

llm = OpenAI()
index_name = "rag2"
embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

def rag_decision(conversation_id):
    prompt_stack = [
        {"role": "system", "content": prompt_config.rag_decision},
        *history.database[conversation_id]
    ]

    completion = llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt_stack
    )

    content = completion.choices[0].message.content
    decision = json.loads(content)
    print(decision)
    return decision

def rag(text, k=4):
    results = vectorstore.similarity_search(text, k=k)
    return results

def compile_documents(results):
    if not results:
        documents_output = ""
    else:
        documents_output = "The following are contextual docs to respond to user, if conversation would benefit from it:\n"
        for i, document in enumerate(results):
            lines = document.page_content.split('\n', 1)
            page_content = lines[0] if len(lines) == 1 else lines[1]
            documents_output += f"Document {i + 1}:\n{page_content}\n\n"
    return documents_output
    
def compile_sources(results):
    sources_list = []
    if results:
        for document in results:
            lines = document.page_content.split('\n', 1)
            source = lines[0].replace('Source: ', '') if len(lines) > 1 else "No source specified"
            sources_list.append(source)
    return sources_list

def rag_results(user_input, conversation_id):
    decision = rag_decision(conversation_id)

    if decision==1: 
        documents = rag(user_input, k=4)
        concat_docs = compile_documents(documents)
        sources = compile_sources(documents)
    else: 
        concat_docs = ""
        sources = []

    return concat_docs, sources