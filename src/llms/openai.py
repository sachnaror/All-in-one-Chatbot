import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
  def __init__(self, user_controls_input):
    self.user_controls_input = user_controls_input
    
  def get_llm_model(self):
    try:
      openai_api_key = self.user_controls_input['API Key']
      openai_model = self.user_controls_input['Selected Model']

      if openai_api_key == "":
        st.error('Please enter your OpenAI API key to proceed.')

      llm = ChatOpenAI(model=openai_model, openai_api_key=openai_api_key)
      return llm

    except KeyError as e:
      st.error(f"Missing configuration: {e}")
      return None