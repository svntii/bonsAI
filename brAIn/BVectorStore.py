import os
import getpass
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters.base import TextSplitter

from langchain_community.vectorstores.chroma import Chroma
from langchain_core.embeddings import Embeddings


from BHistorian import *


load_dotenv("../.env")
os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')




class BVectorStore:
    '''
        bonsAI implementation of vector
        responsble for 


        reference: 
        https://developer.dataiku.com/latest/tutorials/machine-learning/genai/nlp/gpt-lc-chroma-rag/index.html
    
    '''



    def __init__(self, pathToText, model: BHistorian, textSplitter: TextSplitter = CharacterTextSplitter(), embeddings: Embeddings = OpenAIEmbeddings()) -> None:
        
        self.model = model
        self.emb = embeddings(model.getModel())        
        self.ts = textSplitter

        self.db = self.textLoad(pathToText,textSplitter=self.ts, embeddings=self.emb)
        self.retriever = self.db.as_retriever()


    def textLoad(self, path: str, textSplitter: TextSplitter, embeddings: Embeddings):

        raw = TextLoader(path).load()
        splitDocs = textSplitter.split_documents(raw)
        db = Chroma.from_documents(documents=splitDocs, embedding=OpenAIEmbeddings())

        return db
    

  









