from fastapi import APIRouter, Response, Body, status
import jsonschema
from backend.schema import PROMPT_SCHEMA
from backend.agent import chain
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/chat"
)

class ChatResponse(BaseModel):
    id: int
    responseText: str
    userResponseSuggestions: List[str]

'''
Input looks like:
POST
{"prompt": "<user input>"}
'''
@router.post("", response_model=ChatResponse)
def invoke_agent(response: Response, body: dict = Body(...)):
    try:
        jsonschema.validate(body, PROMPT_SCHEMA)
    except jsonschema.ValidationError as error:
        print(error)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error.message}
    
    # response = chain.invoke({"input": body["prompt"]})

    # print(response)

    # return {
    #     "completion": response.content
    # }
    response = {
        'id' : 1,
        'responseText' : "Successful response with id",
        'userResponseSuggestions' : ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    }
    return ChatResponse(**response)

@router.post("/{id}", response_model=ChatResponse)
def invoke_agent_with_id(response: Response, id: int, body: dict = Body(...)):
    try:
        jsonschema.validate(body, PROMPT_SCHEMA)
    except jsonschema.ValidationError as error:
        print(error)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error.message}
    
    # response = chain.invoke({"input": body["prompt"]})
    response = {
        'id' : id,
        'responseText' : "Successful response with id",
        'userResponseSuggestions' : ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
    }
    return ChatResponse(**response)