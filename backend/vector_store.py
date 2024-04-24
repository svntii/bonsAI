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

index_name = "rag"
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

    source = source.replace('.txt', '')

    for chunk in chunks:
        if chunk:
            content_with_source = f"Source: {source}\n{chunk.page_content}"
            vectorstore.add_texts([content_with_source], metadata={"source": source})

    print(f"Chunks from {source} loaded and added to vectorstore.")

def add_documents(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  
            file_path = os.path.join(folder_path, filename)
            source = filename  # Using filename as source metadata
            load_chunks(file_path, source)

def rag(text, k=4):
    results = vectorstore.similarity_search(text, k=k)
    return results

def print_results(results):
    for i, document in enumerate(results):
        lines = document.page_content.split('\n', 1)
        if len(lines) > 1:
            metadata_line, page_content = lines
            source = metadata_line.replace('Source: ', '') 
            metadata = {"source": source}
        else:
            page_content = lines[0] if lines else 'No content available'
            metadata = {"source": "No source specified"}

        print(f"Document {i + 1}:")
        print(f"\n{page_content}")
        print(f"Metadata: {metadata}")
        print("\n")  

if __name__ == "__main__":

    # doc_folder = "../data"
    # add_documents(doc_folder)

    query_text = "what are the latest hall council updates?"
    k = 4
    results = rag(query_text, k)
    print_results(results)