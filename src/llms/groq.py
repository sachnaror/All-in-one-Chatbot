import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:

  def __init__(self, user_controls_input):
    self.user_controls_input = user_controls_input

  def get_llm_model(self):
    try:
      groq_api_key = self.user_controls_input['API Key']
      groq_model = self.user_controls_input['Selected Model']

      if groq_api_key== "":
        st.error('Please enter your Groq API key to proceed.')

      llm = ChatGroq(model=groq_model, api_key=groq_api_key)
      return llm
    
    except KeyError as e:
      st.error(f"Missing configuration: {e}")
      return None
    
    