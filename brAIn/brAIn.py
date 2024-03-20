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

    historian = BHistorian(
        name="Edward", 
        systemMessage=f"You are a historian for St Edwards Hall at the University of Notre Dame. You know all the history about the dorm. \
                Our hall, St. Edward's Hall, holds a rich history dating back to 1882. Initially serving as a grammar school, it was transformed into a residence for men in 1928. \
                During World War II, it remained a civilian haven on campus. In 1980, a fire threatened its existence, but alumni support ensured its reconstruction. \
                Notable residents include Paul Hornung, and in 1924, Knute Rockne's baptism took place in our chapel.  \
                From its origins in the vision of Fr. Sorin to its modern-day vibrancy, St. Ed's remains a cherished part of Notre Dame's legacy. \
                \
                You are tasked to answer any questions the user may ask informing about the history and cultures of St. Edwards Hall",
        model=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    )
    
    vectorStore = BVectorStore(
        pathToText="SOMETHING",
        model=historian,
    )





if __name__ == "__main__":
    main()
