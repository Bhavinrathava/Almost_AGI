import json

from jinja2 import Environment, BaseLoader

from LLM.llm import LLM

PROMPT = open("Agents/Executor/prompt.jinja2").read().strip()

class Decision:
    def __init__(self, base_model: str):
        self.llm = LLM(model_name=base_model)

    def render(self, prompt: str) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(prompt=prompt)

    def validate_response(self, response: str):
        for item in response:
            if "function" not in item or "args" not in item or "reply" not in item:
                return False
        
        return response

    def execute(self, prompt: str, project_name: str) -> str:
        rendered_prompt = self.render(prompt)
        response = self.llm.inference(rendered_prompt)
        
        valid_response = self.validate_response(response)

        return valid_response