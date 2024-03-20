from openai import OpenAI
from BVectorStore import BVectorStore
### Private

class _BHistorianOutput:
    pass



### PUBLIC

class BHistorian:

    def __init__(self, name, model: OpenAI) -> None:
        # TODO try maybe llama 
        
        self.name = name
        self.soul = model
        self.store = None
    

    def getModel(self):
        return self.soul
    

    def load_store(self, store: BVectorStore):
        self.store = store

    def userPrompt(self, prompt: str, k=5) -> any:        
        if self.store is None:
            print("ERROR: No Store :(")

        promptEmb = self.store.emb.embed_query(prompt)
        similarDocs = self.store.db.similarity_search(query=promptEmb)
        prompt = " ".join([doc.text for doc in similarDocs[:k]])

        result = self.soul.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt # TODO: LOOK OVER
        )

        return result.choices[0].message.content

class BHistorianInput:
    pass

class BHistorianResponse:

    def __init__(self, response: str):
        
        self.response = response