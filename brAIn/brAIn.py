# brAIn.py


from BHistorian import *
from BVectorStore import *  

from dotenv import load_dotenv
import os

CONFIG = "../config.yaml"

'''
# TODO

    -   define interface for historian
    -   define interface for VectorStore
    -   UI/UX

'''



def main():
    load_dotenv()
    config = BConfig.from_yaml(CONFIG)
    

    historian = BHistorian(
        name=config.historian.name, 
        systemMessage=config.historian.systemMessage,
        model=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    )

    vectorStore = BVectorStore(
        pathToText=config.vectorStore.toText,
        model=historian,
    )





if __name__ == "__main__":
    main()
