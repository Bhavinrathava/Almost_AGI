import openai
import os 
from dotenv import load_dotenv
load_dotenv()

class OpenAIModel:
    def __init__(self, api_key, model_name="gpt-3.5-turbo-0125"):
        self.api_key = api_key
        self.model_name = model_name
        openai.api_key = self.api_key

    def inference(self, prompt: str):
        response = openai.chat.completions.create(
            model =self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    api_key = os.environ.get("OPENAI_KEY")
    openai_model = OpenAIModel(api_key)  # Use a different name here
    prompt = "Once upon a time"
    print(openai_model.inference(prompt))
