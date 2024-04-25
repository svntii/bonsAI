from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
import os

'''
Pinecone x Langchain Integration
More info: https://docs.pinecone.io/integrations/langchain
https://api.python.langchain.com/en/latest/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html
'''

index_name = "rag2"
embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

def load_chunks(filename, source):
    loader = TextLoader(filename)
    documents = loader.load()
    if documents is None or not documents:
        print(f"No content found in {filename}")
        return
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    for chunk in chunks:
        if chunk:
            content_with_source = f"Source: {source}\n{chunk.page_content}"
            vectorstore.add_texts([content_with_source], metadata={"source": source})

    print(f"Chunks from {source} loaded and added to vectorstore.")

def add_documents(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  
            file_path = os.path.join(folder_path, filename)
            source = filename.replace('.txt', '').replace('_', ' ')
            load_chunks(file_path, source)

if __name__ == "__main__":
    doc_folder = "../data_2"
    add_documents(doc_folder)