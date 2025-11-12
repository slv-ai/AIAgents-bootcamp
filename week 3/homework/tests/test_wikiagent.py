from .utils import get_tool_call
import main

def test_get_page_invoked_multiple_times():
    result=main.run_agent_sync("where do capybaras live")
    tool_call = get_tool_call(result)
    assert len(tool_call) > 1 ,"Expected multiple tool calls for 'get_page'"