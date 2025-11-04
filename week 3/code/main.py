import search_agent
import asyncio

agent= search_agent.create_Agent()
agent_callback = search_agent.NamedCallBack(agent)

async def run_agent(user_prompt:str):
    response = await agent.run(
        user_prompt,
        event_stream_handler= agent_callback
    )
    return response

response = asyncio.run(run_agent("What is llm evaluation?"))
print(response.output)

