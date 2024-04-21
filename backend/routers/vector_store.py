from fastapi import APIRouter, HTTPException, Body
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.embeddings import Embeddings

from dotenv import load_dotenv
import os
import httpx

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("No key found")

path_to_text_file = "data/steds.txt"
router = APIRouter(prefix="/vectorstore")

'''
Chroma methods:
https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.chroma.Chroma.html#langchain_community.vectorstores.chroma.Chroma.asimilarity_search
'''

class VectorStoreManager:
    def __init__(self, path: str, embeddings: Embeddings):
        self.emb = embeddings
        self.textSplitter = CharacterTextSplitter()
        self.db = self.load_text(path)
    
    def load_text(self, path: str):
        raw = TextLoader(path, encoding="utf-8").load()
        split_docs = self.textSplitter.split_documents(raw)
        db = Chroma.from_documents(documents=split_docs, embedding=self.emb)
        return db

    def add_documents(self, documents: list):
        for document in documents:
            self.db.aadd_texts(document)

    def rag(self, query_text, k=5):
        query_embedding = self.get_openai_embedding(query_text)
        docs = self.db.similarity_search_by_vector(query_embedding, k=k) 
        return docs

    def get_openai_embedding(self, text: str):
        url = "https://api.openai.com/v1/embeddings"
        headers = {
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "input": text,
            "model": "text-embedding-ada-002"
        }
        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to get embeddings from OpenAI")
        return response.json()["data"][0]["embedding"]

@router.post("/add")
async def add_to_store(data: list = Body(...)):
    try:
        vector_store.add_documents(data)
        return {"message": "Documents successfully added to vector store"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/rag")
def retrieve_documents(query: str, k: int = 5):
    return vector_store.rag(query, k)

model_name = "text-embedding-ada-002"
openai_embeddings = OpenAIEmbeddings(api_key=openai_api_key, model=model_name)
vector_store = VectorStoreManager(path_to_text_file, embeddings=openai_embeddings)