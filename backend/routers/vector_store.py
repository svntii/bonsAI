from fastapi import FastAPI, HTTPException, Request
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pydantic import BaseModel

import os

app = FastAPI()

# Initialize PineconeVectorStore
index_name = "my-index"
embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

# Models for the API
class Documents(BaseModel):
    texts: list[str]

class Query(BaseModel):
    text: str
    k: int = 4 

@app.post("/add-documents/")
async def add_documents(docs: Documents):
    try:
        for doc in docs.documents:
            vectorstore.add_texts([doc.text])
        return {"message": "Documents added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/retrieve-similar/")
async def retrieve_similar(text: str, k: int = 4):
    try:
        results = vectorstore.similarity_search(text, k=k)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)