from jinja2 import Environment, BaseLoader
from LLM.llm import LLM
PROMPT = open("Agents/Planner/prompt.jinja2").read().strip()

class Planner:
    def __init__(self, model_name, base_model, base_url = "http://localhost:11434"):
        self.llm = LLM(model_name = model_name, model_type=base_model, base_url=base_url)

    def render(self, prompt: str) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(prompt=prompt)
    
    def validate_response(self, response: str) -> bool:
        return True
    
    def parse_response(self, response: str):
        result = {
            "reply": "",
            "focus": "",
            "plans": {},
            "summary": ""
        }

        current_section = None
        current_step = None

        for line in response.split("\n"):
            line = line.strip()
           
            if line.startswith("Your Reply to the Human Prompter:"):
                current_section = "reply"
                result["reply"] = line.split(":", 1)[1].strip()
            elif line.startswith("Current Focus:"):
                current_section = "focus"
                result["focus"] = line.split(":", 1)[1].strip()
            elif line.startswith("Plan:"):
                current_section = "plans"
            elif line.startswith("Summary:"):
                current_section = "summary"
                result["summary"] = line.split(":", 1)[1].strip()
            elif current_section == "reply":
                result["reply"] += " " + line
            elif current_section == "focus":
                result["focus"] += " " + line
            elif current_section == "plans":
                if line.startswith("- [ ] Step"):
                    current_step = line.split(":")[0].strip().split(" ")[-1]
                    result["plans"][int(current_step)] = line.split(":", 1)[1].strip()
                elif current_step:
                    result["plans"][int(current_step)] += " " + line
            elif current_section == "summary":
                result["summary"] += " " + line.replace("```", "")

        result["reply"] = result["reply"].strip()
        result["focus"] = result["focus"].strip()
        result["summary"] = result["summary"].strip()

        return result    

    def execute(self, prompt: str) -> str:
        prompt = self.render(prompt)
        response = self.llm.inference(prompt)
        return response
    


if __name__ == "__main__":
    planner = Planner("gpt-3.5-turbo")
    prompt = "You are a human prompter. You have been given a task to write a plan for a project. You need to write a plan for a project that involves building a house. The project should include the following steps: 1. Design the house 2. Get the necessary permits 3. Hire a contractor 4. Build the house 5. Inspect the house 6. Move in"
    response = planner.execute(prompt)
    result = planner.parse_response(response)
    print(result)