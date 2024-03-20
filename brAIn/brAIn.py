# brAIn.py


from BHistorian import *
from BVectorStore import *  

from dotenv import load_dotenv
import os


'''
# TODO

    -   define interface for historian
    -   define interface for VectorStore
    -   UI/UX

'''



def main():
    load_dotenv()

    historian = BHistorian("Edward", OpenAI(api_key=os.getenv('OPENAI_API_KEY')))
    vectorStore = BVectorStore(
        pathToText="SOMETHING",
        model=historian,
    )





if __name__ == "__main__":
    main()
