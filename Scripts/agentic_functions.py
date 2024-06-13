from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
import os
from dotenv import load_dotenv
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

class AgenticFunctions:
    def __init__(self):

        load_dotenv()
        self.wolfram = WolframAlphaAPIWrapper()
        self.search = GoogleSearchAPIWrapper()
        self.wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        self.search_tool = Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=self.search.run,
    )

    def searchWithGoogle(self, query: str) -> str:
        return self.search_tool.run(query)
    
    def callWolframAlpha(self, query: str) -> str:
        return self.wolfram.run(query)
    
    def callWikipedia(self, query: str) -> str:
        return self.wikipedia.run(query)
    


if __name__ == "__main__":
    agentic = AgenticFunctions()
    print(agentic.searchWithGoogle("What is the capital of France?"))
    print(agentic.callWolframAlpha("What is 1 + 3?"))
    print(agentic.callWikipedia("France"))
    
