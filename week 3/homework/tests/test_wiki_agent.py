from tests.utils import get_tool_call
import main

def test_get_page_invoked_multiple_times():
    result=main.run_agent_sync("where do capybaras live")
    tool_call = get_tool_call(result)
    assert len(tool_call) > 1 ,"Expected multiple tool calls for 'get_page'"

def test_references_included():
    result=main.run_agent_sync("where do capybaras live")
    assert "## References" in result.final_response, "Expected 'References' section in the final response"

def test_search_invoked_first():
    result=main.run_agent_sync("where do capybaras live")
    tool_call = get_tool_call(result)
    assert tool_call[0].part.tool_name == "search", "Expected 'search' to be the first tool called"