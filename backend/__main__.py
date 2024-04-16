import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL")
port = int(os.getenv("PORT"))

uvicorn.run("backend:app", host=url, port=port, reload=True)