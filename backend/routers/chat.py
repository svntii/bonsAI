from fastapi import APIRouter, Response, Body, status
import jsonschema
from uuid import uuid4
from backend.schema import PROMPT_SCHEMA
from backend import conversation, agent

router = APIRouter(
    prefix="/chat"
)

@router.post("")
def new_conversation(response: Response):
    conversation_id = str(uuid4())

    conversation.history[conversation_id] = []

    print(conversation.history)

    return {
        "id": conversation_id
    }

'''
Input looks like:
POST
{"prompt": "<user input>"}
'''
@router.post("/{conversation_id}")
def invoke_agent(response: Response, conversation_id: str, body: dict = Body(...)):
    try:
        jsonschema.validate(body, PROMPT_SCHEMA)
    except jsonschema.ValidationError as error:
        print(error)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error.message}
    
    print(conversation_id)
    print(conversation.history)
    
    history = conversation.history.get(conversation_id, None)

    if history is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "conversation id not found"}

    user_prompt = body["prompt"]    
    bot_response = agent.invoke(body["prompt"])

    history.append({
        "user": user_prompt,
        "bot": bot_response
    })

    print(bot_response)


    return {
        "completion": bot_response
    }
    


