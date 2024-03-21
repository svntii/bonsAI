from openai import OpenAI
import yaml

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters.base import TextSplitter

from langchain_community.vectorstores.chroma import Chroma
from langchain_core.embeddings import Embeddings

### Private

class _BHistorianOutput:
    pass



### PUBLIC


class BVectorStore:
    '''
        bonsAI implementation of vector
        responsble for 


        reference: 
        https://developer.dataiku.com/latest/tutorials/machine-learning/genai/nlp/gpt-lc-chroma-rag/index.html
    
    '''



    def __init__(self, pathToText, model,  embeddings: Embeddings, textSplitter: TextSplitter = CharacterTextSplitter()) -> None:
        
        self.model = model
        self.emb = embeddings    
        self.ts = textSplitter

        self.db = self.textLoad(pathToText,textSplitter=self.ts, embeddings=self.emb)
        self.retriever = self.db.as_retriever()


    def textLoad(self, path: str, textSplitter: TextSplitter, embeddings: Embeddings):

        raw = TextLoader(path, encoding="utf-8").load()
        splitDocs = textSplitter.split_documents(raw)
        db = Chroma.from_documents(documents=splitDocs, embedding=OpenAIEmbeddings())

        return db
    

  


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

    def system_ask(self, prompt):
        self.msgs.append({"role": "assistant", "content": prompt})

        result = self.soul.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.msgs # TODO: LOOK OVER
        )
        reply = result.choices[0].message.content        
        self.msgs.append({"role": "assistant", "content": reply})

        return reply


    def ask(self, prompt: str, k=5) -> any:        
        if self.store is None:
            print("ERROR: No Store :(")

        self.msgs.append({"role": "user", "content": prompt})
        
        similarDocs = self.store.db.similarity_search(query=prompt)

        print()
        print("similar docs:")
        print(similarDocs)

        enrichedPrompt = " ".join([doc.page_content for doc in similarDocs[:k]])

        print()
        print("enriched prompt:")
        print(enrichedPrompt)

        self.msgs.append({"role": "user", "content": "Additional information and context has been provided to answer the user's question:\n" + enrichedPrompt})

        for msg in self.msgs:
            print("\t", end="")
            print(msg["role"])
            print(msg["content"])
            print()

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


