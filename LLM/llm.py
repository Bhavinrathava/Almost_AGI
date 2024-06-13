
from LLM.openai_model import OpenAIModel
from LLM.ollama import Ollama
import os 
from dotenv import load_dotenv
load_dotenv()

class LLM:
    def __init__(self, model_name, model_type, base_url = None):
        self.model_name = model_name
        self.model_type = model_type
        self.base_url = base_url
        self.model = self.initiateModel()
        
        

    def inference(self, prompt:str):
        return self.model.inference(prompt)
        
    def initiateModel(self):
        if(self.model_name == "openai"):
            api_key = os.environ.get("OPENAI_KEY")
            return OpenAIModel(api_key=api_key, model_name=self.model_type)
        elif(self.model_name == "ollama"):
            return Ollama(base_url=self.base_url, model_name=self.model_type)
        else:
            return None