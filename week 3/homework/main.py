import wiki_agent
import asyncio
 
agent = wiki_agent.create_agent()
agent_callback = wiki_agent.NamedCallback(agent)
async def run_agent(user_prompt: str):
    results = await agent.run(
        user_prompt=user_prompt,
        event_stream_handler=agent_callback
    )
    return results

result = asyncio.run(run_agent("where do capybaras live"))
print(result.output)