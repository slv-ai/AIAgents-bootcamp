from pydantic_ai import Agent
from pydantic_ai.messages import FunctionToolCallEvent
import search_tools

class NamedCallBack:
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
make atleast 3 search tool calls to find relevant information 
"""
def create_Agent():
    tools= search_tools.prepare_search_tools()
    return Agent(
        name="SearchAgent",
        instructions=search_instructions,
        tools=[tools.search],
        model="gpt-4o-mini",
    )
