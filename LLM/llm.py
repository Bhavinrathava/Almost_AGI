
from LLM.openai_model import OpenAI
from LLM.ollama import Ollama

class LLM:
    def __init__(self, model_name, model_type, base_url = None):
        self.model_name = model_name
        self.model_type = model_type
        self.base_url = base_url
        self.model = self.initiateModel(self.model_name, self.model_type, self.base_url)
        
        

    def inference(self, prompt:str):
        return self.model.inference(prompt)
        
    def initiateModel(self):
        if(self.model_name == "openai"):
            return OpenAI()
        elif(self.model_name == "ollama"):
            return Ollama(base_url=self.base_url, model_name=self.model_type)
        else:
            return None