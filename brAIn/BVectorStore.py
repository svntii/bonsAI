import os
import getpass
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters.base import TextSplitter

from langchain_community.vectorstores.chroma import Chroma
from langchain_core.embeddings import Embeddings



load_dotenv("../.env")
os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')




class BVectorStore:

    def __init__(self, pathToText, textSplitter: TextSplitter, embeddings: Embeddings) -> None:
        
        self.db = self.textLoad(pathToText,textSplitter=textSplitter, embeddings=embeddings)


    def textLoad(self, path: str, textSplitter: TextSplitter, embeddings: Embeddings):

        raw = TextLoader(path).load()
        splitDocs = textSplitter.split_documents(raw)
        db = Chroma.from_documents(documents=splitDocs, embedding=OpenAIEmbeddings())

        return db

    def similarSearch(self, query):
        
        result = self.db.similarity_search(query=query)
        return result









