

### Private

class _BHistorianOutput:
    pass



### PUBLIC

class BHistorian:

    def __init__(self, name) -> None:
        
        self.name = name
    

    def userPrompt(self, prompt: str) -> any:
        pass



class BHistorianInput:
    pass

class BHistorianResponse:

    def __init__(self, response: str):
        
        self.response = response