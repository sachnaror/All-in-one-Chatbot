from src.state.state import State
from src.tools.websearch import WebSearchTool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain.tools import BaseTool

class WebSearchChatbot:
    def __init__(self, model, session_id: str = "default", tavily_api_key: str = None):
        self.model = model
        self.session_id = session_id
        self.memory_config = {"configurable": {"session_id": session_id}}
        
        if tavily_api_key and tavily_api_key.strip():
            try:
                self.web_search = WebSearchTool(tavily_api_key)
                self.tools = [self.web_search.get_tool()]
                self.model_with_tools = model.bind_tools(self.tools)
                self.has_search = True
            except Exception as e:
                self.model_with_tools = model
                self.has_search = False
        else:
            self.model_with_tools = model
            self.has_search = False

    def process(self, state):
        messages = state['messages']
        if not messages:
            return state
        
        if not self.has_search:
            # If no search capability, add a message about it
            last_message = messages[-1]
            if hasattr(last_message, 'content') and any(keyword in last_message.content.lower() for keyword in ['search', 'find', 'latest', 'current', 'news']):
                search_disclaimer = "I don't have web search capabilities enabled. Please provide a Tavily API key to search for current information."
                response_content = f"{search_disclaimer}\n\nBased on my training data, I can still help with general questions."
                from langchain_core.messages import AIMessage
                return {'messages': AIMessage(content=response_content)}
        
        response = self.model_with_tools.invoke(messages, config=self.memory_config)
        
        if hasattr(response, 'tool_calls') and response.tool_calls:
            messages.append(response)
            
            for tool_call in response.tool_calls:
                tool_result = self._execute_tool_call(tool_call)
                tool_message = ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call['id']
                )
                messages.append(tool_message)
            
            final_response = self.model_with_tools.invoke(messages, config=self.memory_config)
            return {'messages': final_response}
        
        return {'messages': response}
    
    def _execute_tool_call(self, tool_call):
        if tool_call['name'] == 'tavily_search_results_json':
            return self.web_search.search_tool.invoke(tool_call['args'])
        return "Tool not found"
