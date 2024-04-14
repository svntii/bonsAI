from fastapi import APIRouter, Response, Body, status
import jsonschema
from backend.schema import PROMPT_SCHEMA
from backend.agent import llm

router = APIRouter(
    prefix="/chat"
)


'''
Input looks like:
POST
{"prompt": "<user input>"}
'''
@router.post("")
def invoke_agent(response: Response, body: dict = Body(...)):
    try:
        jsonschema.validate(body, PROMPT_SCHEMA)
    except jsonschema.ValidationError as error:
        print(error)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error.message}
    
    return {
        "completion": llm.invoke(body["prompt"])
    }
    


