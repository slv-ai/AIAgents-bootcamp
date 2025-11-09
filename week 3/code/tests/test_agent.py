from tests.utils import get_tool_call

import main

def test_agent_makes_3_tool_calls():
    user_prompt = "What is the llm evaluation?"
    result=main.run_agent_sync(user_prompt)
    print(result.output)
    messages =result.new_messages()
    tool_calls = get_tool_call(result)
    assert len(tool_calls) >= 3, "Agent did not make at least 3 tool calls"

if __name__ == "__main__":
    test_agent_makes_3_tool_calls()