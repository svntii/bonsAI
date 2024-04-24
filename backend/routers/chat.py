from fastapi import APIRouter, Response, Body, status
import jsonschema
from uuid import uuid4
from backend.schema import PROMPT_SCHEMA
from backend.agent import chain
from backend import conversation
from typing import List
from pydantic import BaseModel

class initChatResponse(BaseModel):
    id: str
    response: str
    suggested_responses: List[str]

class chatResponse(BaseModel):
    response: str
    sources: List[str]
    suggested_responses: List[str]

router = APIRouter(
    prefix="/chat"
)
@router.post("", response_model=initChatResponse)
def new_conversation(response: Response):
    conversation_id = str(uuid4())

    # conversation.history[conversation_id] = []

    # print(conversation.history)

    # return {
    #     "id": conversation_id
    # }
    response = "successful initial response"
    suggestions = ["Suggestion 1", "Suggestion 2", "Suggestion 3"]

    return initChatResponse(id=conversation_id, response=response, suggested_responses=suggestions)

'''
Input looks like:
POST
{"prompt": "<user input>"}
'''

@router.post("/{conversation_id}", response_model=chatResponse)
def invoke_agent(response: Response, conversation_id: str, body: dict = Body(...)):
    
    try:
        jsonschema.validate(body, PROMPT_SCHEMA)
    except jsonschema.ValidationError as error:
        print(error)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error.message}

    """
    print(conversation_id)
    print(conversation.history)
    
    history = conversation.history.get(conversation_id, None)

    if history is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "conversation id not found"}

    user_prompt = body["prompt"]    
    invocation = chain.invoke({"input": body["prompt"]})
    bot_response = invocation["content"]

    history.append({
        "user": user_prompt,
        "bot": bot_response
    })

    print(bot_response)


    return {
        "completion": bot_response
    }
    """
    response = "Successful subsequent response"
    suggestions = ["Successful initial response", "Suggestion 1", "Suggestion 2", "Suggestion 3"]
    sources= ["source1", "source 2", "source 3"]

    return chatResponse(response=response, sources=sources, suggested_responses=suggestions)
    


