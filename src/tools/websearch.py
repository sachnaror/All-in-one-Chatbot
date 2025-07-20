from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
import os

class WebSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not api_key:
            raise ValueError("Tavily API key is required for web search functionality")
        
        # Set the API key as environment variable for TavilySearchResults
        os.environ["TAVILY_API_KEY"] = api_key
        
        self.search_tool = TavilySearchResults(
            max_results=5
        )
    
    def search_web(self, query: str) -> str:
        """Search the web for current information about the given query."""
        try:
            results = self.search_tool.invoke(query)
            if not results:
                return "No search results found."
                
            formatted_results = []
            for result in results:
                if isinstance(result, dict):
                    title = result.get('title', 'N/A')
                    content = result.get('content', 'N/A')
                    url = result.get('url', 'N/A')
                    formatted_results.append(f"Title: {title}\nContent: {content}\nURL: {url}\n")
                else:
                    formatted_results.append(str(result))
            
            return "\n".join(formatted_results)
        except Exception as e:
            return f"Error searching the web: {str(e)}"
    
    def get_tool(self):
        return self.search_tool
