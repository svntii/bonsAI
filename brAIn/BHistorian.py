from openai import OpenAI
from BVectorStore import BVectorStore
import yaml


### Private

class _BHistorianOutput:
    pass



### PUBLIC

class BHistorian:

    def __init__(self, name, systemMessage, model: OpenAI) -> None:
        # TODO try maybe llama 
        
        self.name = name
        self.soul = model
        self.store = None
        self.sysMes = systemMessage
        self.msgs = [{"role": "system", "content": self.sysMes}]
    

    def getModel(self):
        return self.soul
    

    def load_store(self, store: BVectorStore):
        self.store = store

    def ask(self, prompt: str, k=5) -> any:        
        if self.store is None:
            print("ERROR: No Store :(")

        promptEmb = self.store.emb.embed_query(prompt)
        similarDocs = self.store.db.similarity_search(query=promptEmb)
        prompt = " ".join([doc.text for doc in similarDocs[:k]])

        self.msgs.append({"role": "user", "content": prompt})


        result = self.soul.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.msgs # TODO: LOOK OVER
        )
        reply = result.choices[0].message.content        
        self.msgs.append({"role": "assistant", "content": reply})

        return reply

    def reset(self):
        self.msgs = []
        self.msgs.append({"role": "system", "content": self.sysMes})

class BHistorianInput:
    pass

class BHistorianResponse:

    def __init__(self, response: str):
        
        self.response = response


class BConfig:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, BConfig(**value))  # Recursively create nested Config objects
            else:
                setattr(self, key, value)

    @staticmethod
    def from_yaml(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return BConfig(**config)
