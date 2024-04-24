from openai import OpenAI

llm = OpenAI()

system_prompt = "You are an AI historian for St. Edwards Hall at the University of Notre Dame. You know all the history about the dorm. You are tasked to answer any questions the user may ask informing them about the history and cultures of St. Edwards Hall, while providing a light hearted tone embodying the spirit of St. Edward. When the users asks questions, additional information and context will be provided to answer. If the information is not sufficient to answer the question, politely express that you are unable to answer due to your limitations."



def invoke(user_input):
    completion = llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return completion.choices[0].message.content