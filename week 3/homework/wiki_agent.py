from pydantic_ai import Agent
from pydantic_ai.messages import FunctionToolCallEvent
import tools
from tools import search, get_page

class NamedCallback:
    def __init__(self,agent):
        self.agent_name = agent.name 
    async def print_function_calls(self,ctx,event):
        #detect nested streams
        if hasattr(event,"__aiter__"):
            async for e in event:
                await self.print_function_calls(ctx,e)
            return
        if isinstance(event,FunctionToolCallEvent):
            tool_name = event.part.tool_name
            args=event.part.args
            print(f"Agent {self.agent_name} called function:{tool_name} with args: {args}")

    async def __call__(self,ctx,event):
        return await self.print_function_calls(ctx,event)


search_instructions = """
"You are a helpful Wikipedia research assistant. "
        "When answering questions, you should:\n"
        "1. First search Wikipedia for relevant articles\n"
        "2. Retrieve and read multiple relevant pages\n"
        "3. Synthesize information from the pages to answer the question\n"
        "4. Always include 'References' to the Wikipedia pages you used in the format:
         ## References (https://en.wikipedia.org/wiki/Capybara) \n"
        "5. Be concise but informative in your answers"
"""

def create_agent():
    
    return Agent(
        name="wiki_agent",
        instructions=search_instructions,
        tools=[search,get_page],
        model="openai:gpt-4o-mini",
    )
