# YOu will have prompt from the user 

# Send to the Planner agent along with the model name to get the task list 

# Initiate 2 Queues : CompletedTasks and PendingTasks

# Send the first task from the PendingTasks to the Executor 
# agent along with the model name to get the function chain for that task 

# Based on the response from above, call the functions and append their results to the 

from Agents.Composer import Composer
from Agents.Executor import Executor
from Agents.FeedBack import FeedBack
from Agents.Planner import Planner
from collections import deque
from Agents.Executor.executor import callFunction
def getAnswer(prompt, model_name):

    planner = Planner(model_name)
    executor = Executor(model_name)

    response = planner.execute(prompt)
    result = planner.parse_response(response)
    
    pendingTasks = deque()

    for key, value in result["plans"].items():
        pendingTasks.append(value)

    
    completedTasks = deque()

    while len(pendingTasks) > 0:
        task = pendingTasks.popleft()
        response = executor.execute(task)
        functionChain = executor.validate_response(response)
        
        for item in functionChain:
            # Item = {"function_name": "function_name", "args": "args", "reply": "reply"}
            callResult = callFunction(item["function_name"], item["args"])
            item['result'] = callResult
        
        feedback = FeedBack(model_name)
        feedbackresponse = feedback.execute(task, functionChain)
        feedbackresponse = feedback.validate_response(feedbackresponse)
        feedbackresponse = feedback.parse_response(feedbackresponse)

        if(feedbackresponse['status'] == "success"):
            task["history"] = functionChain
            completedTasks.append(task)

    composer = Composer(model_name)
    response = composer.execute(prompt, completedTasks)

    response = composer.validate_response(response)
    response = composer.parse_response(response)

    return response['reply']

    
    

