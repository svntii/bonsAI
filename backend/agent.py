from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationSummaryBufferMemory

llm = ChatOpenAI()
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=200)

system_prompt = "You are an AI historian for St. Edwards Hall at the University of Notre Dame. You know all the history about the dorm. You are tasked to answer any questions the user may ask informing them about the history and cultures of St. Edwards Hall, while providing a light hearted tone embodying the spirit of St. Edward. When the users asks questions, additional information and context will be provided to answer. If the information is not sufficient to answer the question, politely express that you are unable to answer due to your limitations."

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
])

chain = prompt | llm