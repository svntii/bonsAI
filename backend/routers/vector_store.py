from fastapi import APIRouter, HTTPException, Body
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.embeddings import Embeddings

from dotenv import load_dotenv
import os

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
            self.db.aadd_documents(document)

model_name = "text-embedding-ada-002"
openai_embeddings = OpenAIEmbeddings(api_key=openai_api_key, model=model_name)
vector_store = VectorStoreManager(path_to_text_file, embeddings=openai_embeddings)

@router.post("/add")
async def add_to_store(data: list = Body(...)):
    try:
        vector_store.add_documents(data)
        return {"message": "Documents successfully added to vector store"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
