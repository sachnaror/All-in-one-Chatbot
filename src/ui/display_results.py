import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage


class DisplayResults:  
  """Class to display results in the Streamlit UI.""" 
  def __init__(self, user_message, use_case, graph):
    """
    Initialize the DisplayResults with user message, use case, and graph.
    
    :param user_message: The message input by the user.
    :param use_case: The selected use case for the chatbot.
    :param graph: The state graph to be processed.
    """
    self.user_message = user_message
    self.use_case = use_case
    self.graph = graph

  def display_results(self):
    """
    Display the results in the Streamlit UI.
    
    This method processes the user message through the graph and displays the response.
    """
    use_case = self.use_case
    user_message = self.user_message
    graph = self.graph

    if use_case == 'Basic Chatbot':
        for event in graph.stream({'messages':("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)

                