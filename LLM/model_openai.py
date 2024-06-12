import openai
import requests

class OpenAIModel : 
    def __init__(self, api_key, model_name = "gpt-3.5-turbo-0125"):
        self.api_key = api_key
        self.model_name = model_name
        openai.api_key = self.api_key 

    def inference(self, prompt:str):
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip() 

if __name__ == "__main__":
    api_key = "key"
    openai_model = OpenAIModel(api_key)
    prompt = "Once upon a time"
    print(openai_model.inference(prompt))



    