import requests
import json 

class Ollama : 
    def __init__(self, base_url = None, model_name = "llama3"):
        self.base_url = base_url
        self.model_name = model_name

    def inference(self, prompt:str):
        url = f'{self.base_url}/api/generate'
        data = {
            "model": self.model_name,
            "prompt": prompt
        }
        response = requests.post(url, json=data)
        response_content = response.content.decode('utf-8')
        response_lines = response_content.strip().split('\n')
        response = response_lines[0]

        response = json.loads(response)['response']
        return response


if __name__ == "__main__":

    base_url = "http://localhost:11434"
    ollama = Ollama(base_url)

    prompt = "Once upon a time"
    print(ollama.inference(prompt))

