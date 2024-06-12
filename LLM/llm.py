
from LLM.openai_model import OpenAI
from LLM.ollama import Ollama

class LLM:
    def __init__(self, model_name:str):
        self.model_name = model_name
        self.model = self.initiateModel(self.model_name)

    def inference(self, prompt:str):
        return self.model.inference(prompt)
        
    def initiateModel(self, model_name:str):
        if(model_name == "openai"):
            return OpenAI()
        elif(model_name == "ollama"):
            return Ollama()
        else:
            return None