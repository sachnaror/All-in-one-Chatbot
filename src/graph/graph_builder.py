from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.state.state import State
from src.nodes.basic_chatbot import BasicChatbot
from src.nodes.websearch_chatbot import WebSearchChatbot


class GraphBuilder:
    
    """Class to build the state graph for the application."""

    def __init__(self, model, session_id: str = "default", tavily_api_key: str = None):
        self.llm = model
        self.session_id = session_id
        self.tavily_api_key = tavily_api_key
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot(self):
        """Initialize the basic chatbot node in the graph."""
        self.basic_chatbot_node = BasicChatbot(self.llm, self.session_id)
        self.graph_builder.add_node('basic_chatbot', self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, 'basic_chatbot')
        self.graph_builder.add_edge('basic_chatbot', END)                                  

    def websearch_chatbot(self):
        self.websearch_chatbot_node = WebSearchChatbot(self.llm, self.session_id, self.tavily_api_key)
        self.graph_builder.add_node('websearch_chatbot', self.websearch_chatbot_node.process)
        self.graph_builder.add_edge(START, 'websearch_chatbot')
        self.graph_builder.add_edge('websearch_chatbot', END)                                  

    def setup_graph(self, use_case: str):
        """
        Setup the graph with the appropriate nodes based on use case.
        
        :param use_case: The use case for which the graph is being built.
        """
        
        if use_case == 'Basic Chatbot':
            self.basic_chatbot()
        elif use_case == 'Chatbot with Web Search':
            self.websearch_chatbot()
        else:
            self.basic_chatbot()
        
        # Compile and return the graph
        return self.graph_builder.compile()