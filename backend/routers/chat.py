from fastapi import APIRouter, Response, Body, status
import jsonschema
from uuid import uuid4
from backend.schema import PROMPT_SCHEMA
from backend import agent, history, qotd, prompt_config

router = APIRouter(
    prefix="/chat"
)

@router.post("")
def new_conversation(response: Response):
    conversation_id = str(uuid4())

    response = prompt_config.intro_message + "\n\n" + qotd.choose_one()

    history.database[conversation_id] = [
        {"role": "assistant", "content": response}
    ]

    return {
        "id": conversation_id,
        "response": response,
        "suggested_responses": [prompt_config.reject_qotd]
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
    
    if conversation_id not in history.database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "conversation id not found"}

    user_prompt = body["prompt"]    
    bot_response = agent.invoke(user_prompt, conversation_id)

    history.database[conversation_id].extend([
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": bot_response}
    ])
    history.database.save()

    suggested_responses = agent.generated_suggested_responses(conversation_id)

    return {
        "response": bot_response,
        "sources": [],
        "suggested_responses": suggested_responses
    }
    

