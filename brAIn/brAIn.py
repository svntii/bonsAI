# brAIn.py

from brAIn.BonsAI import *
from dotenv import load_dotenv
import os

CONFIG = "./config.yaml"

'''
# TODO

    -   define interface for historian
    -   define interface for VectorStore
    -   UI/UX

'''



def demoBot():
    load_dotenv(dotenv_path="./.env")
    config = BConfig.from_yaml(CONFIG)
    
    historian = BHistorian(
        name=config.historian.name, 
        systemMessage=config.historian.systemMessage,
        model=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    )

    vectorStore = BVectorStore(
        pathToText=config.vectorStore.toText,
        model=historian,
        embeddings=OpenAIEmbeddings()
    )
    historian.load_store(vectorStore)

    return historian





def main():
    load_dotenv(dotenv_path="../.env")
    config = BConfig.from_yaml(CONFIG)
    

    historian = BHistorian(
        name=config.historian.name, 
        systemMessage=config.historian.systemMessage,
        model=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    )

    print("historian made")
    vectorStore = BVectorStore(
        pathToText=config.vectorStore.toText,
        model=historian,
        embeddings=OpenAIEmbeddings()
    )
    print("store loaded")


    historian.load_store(vectorStore)
    reply = historian.ask("Name the Leadership of STEDS hall!")
    print(reply)





if __name__ == "__main__":
    main()
