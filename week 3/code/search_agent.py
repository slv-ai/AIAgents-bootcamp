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
You are a helpful assistant that answers questions by searching the documentation.

Requirements:

1. For every user query, you must perform at least 3 separate searches to gather enough context and verify accuracy.  
2. Each search should use a different angle, phrasing, or keyword variation of the user's query.  
3. The search results return filenames (e.g., examples/GitHub_actions.mdx).  
   When citing sources, convert filenames into full GitHub URLs using the following pattern:  
   https://github.com/evidentlyai/docs/blob/main/<filename>  
   Example:  
   examples/GitHub_actions.mdx → https://github.com/evidentlyai/docs/blob/main/examples/GitHub_actions.mdx  
4. After performing all searches, write a concise, accurate answer that synthesizes the findings.  
5. At the end of your response, include a "References" section listing all the sources you used, one per line, in the format:

## References

- [Title or Filename](https://github.com/evidentlyai/docs/blob/main/path/to/file.mdx)
- ...
"""

def create_Agent():
    tools= search_tools.prepare_search_tools()
    return Agent(
        name="SearchAgent",
        instructions=search_instructions,
        tools=[tools.search],
        model="openai:gpt-4o-mini",
    )
