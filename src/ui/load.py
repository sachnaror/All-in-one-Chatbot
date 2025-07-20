import os
import streamlit as st
from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage
from src.ui.config import LoadConfig

class LoadStreamlitUI:
  def __init__(self):
    self.config = LoadConfig()
    self.user_controls = {}

  def initialize_session(self):
    return {
      'current_step': 'requirements',
      'requirements': "",
      'user_stories': "",
      'po_feedback': "",
      'generated_code': "",
      'review_feedback': "",
      'decision': None,
    }
  
  
  def load_ui(self):
    st.set_page_config(page_title=" 🤖" + self.config.get_title(), page_icon=":robot_face:", layout="wide")
    st.header(" 🤖" + self.config.get_title())
    st.session_state.timeframe = ''
    st.session_state.IsFetchButtonClicked = False
    st.session_state.IsSDLC = False

    with st.sidebar:

      llm_options = self.config.get_llm_options()

      # LLM Selection
      self.user_controls['Selected LLM'] = st.selectbox('Select LLM', llm_options)

      if self.user_controls['Selected LLM'] == 'Groq':
        # Groq Model Selection
        groq_models = self.config.get_groq_models()
        self.user_controls['Selected Model'] = st.selectbox('Select Groq Model', groq_models)

        self.user_controls['API Key'] = st.text_input('Enter Groq API Key', type='password')

        if not self.user_controls['API Key']:
            st.warning('Please enter a valid Groq API key to proceed . If you don\'t have an API key, please visit https://console.groq.com to create one.')

      
      if self.user_controls['Selected LLM'] == 'OpenAI':
        # OpenAI Model Selection
        openai_models = self.config.get_openai_models()
        self.user_controls['Selected Model'] = st.selectbox('Select OpenAI Model', openai_models)

        self.user_controls['API Key'] = st.text_input('Enter OpenAI API Key', type='password')

        if not self.user_controls['API Key']:
            st.warning('Please enter a valid OpenAI API key to proceed . If you don\'t have an API key, please visit https://platform.openai.com/account/api-keys to create one.')

      use_case = self.config.get_use_case()

      # Use Case Selection
      self.user_controls['Selected Use Case'] = st.selectbox('Select Use Case', use_case)

      # Tavily API Key for Web Search
      if self.user_controls['Selected Use Case'] == 'Chatbot with Web Search':
          self.user_controls['Tavily API Key'] = st.text_input('Enter Tavily API Key for Web Search', type='password')
          if not self.user_controls['Tavily API Key']:
              st.warning('Tavily API key is required for web search functionality. Get one at https://tavily.com')

      # Memory Management Section
      st.divider()
      st.subheader("💭 Memory Management")
      
      # Display current session ID
      if "session_id" in st.session_state:
          st.text(f"Session: {st.session_state.session_id[-8:]}")  # Show last 8 characters
      
      # Clear conversation button
      if st.button("🗑️ Clear Conversation", help="Clear chat history and start fresh"):
          if "messages" in st.session_state:
              st.session_state.messages = []
          if "memory_manager" in st.session_state and "session_id" in st.session_state:
              # Clear the session from memory manager
              st.session_state.memory_manager.clear_session(st.session_state.session_id)
              # Create new session ID
              st.session_state.session_id = f"user_{hash(str(st.session_state))}"
          st.rerun()


    if 'state' not in st.session_state:
      st.session_state.state = self.initialize_session()

    return self.user_controls
  

