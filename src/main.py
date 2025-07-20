import streamlit as st
import json

from src.ui.load import LoadStreamlitUI
from src.llms.groq import GroqLLM
from src.llms.openai import OpenAILLM
from src.graph.graph_builder import GraphBuilder
from src.ui.display_results import DisplayResults
from src.memory.memory_manager import MemoryManager
from langchain_core.messages import HumanMessage, AIMessage

def load_app():
    """
    Load the Streamlit application.
    """
    
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.error("Failed to load the UI. Please check your configuration.")
        return
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize session ID for memory
    if "session_id" not in st.session_state:
        st.session_state.session_id = f"user_{hash(str(st.session_state))}"
    
    # Initialize memory manager
    if "memory_manager" not in st.session_state:
        st.session_state.memory_manager = MemoryManager()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input at the bottom
    if prompt := st.chat_input("Enter your message..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Process the message
        user_message = prompt
        try:
            # Get the selected LLM provider from user input
            selected_llm = user_input.get('Selected LLM')
            
            # Initialize the appropriate LLM class based on user selection
            if selected_llm == 'Groq':
                llm = GroqLLM(user_controls_input=user_input)
            elif selected_llm == 'OpenAI':
                llm = OpenAILLM(user_controls_input=user_input)
            else:
                st.error("Please select a valid LLM provider (Groq or OpenAI).")
                return
            
            # Get the model instance
            model = llm.get_llm_model()
            
            if not model:
                st.error(f"Failed to initialize the {selected_llm} model. Please check your API key and model selection.")
                return
            
            use_case = user_input.get('Selected Use Case')

            if not use_case:
                st.error("Error: No use case selected.")
                return 
          
            # Use memory-enabled model instead of regular model
            memory_manager = st.session_state.memory_manager
            memory_enabled_model, memory_config = memory_manager.create_memory_enabled_model(
                model, st.session_state.session_id
            )
            
            tavily_api_key = user_input.get('Tavily API Key', '')
            
            graph_builder = GraphBuilder(
                model=memory_enabled_model, 
                session_id=st.session_state.session_id,
                tavily_api_key=tavily_api_key
            )

            try:
                graph = graph_builder.setup_graph(use_case=use_case)
                
                # Process the message through the graph with memory
                ai_response = ""
                # Pass just the current message, memory will handle history
                for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                    for value in event.values():
                        ai_response = value['messages'].content
                
                # Add AI response to chat history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
                # Display AI response
                with st.chat_message("assistant"):
                    st.write(ai_response)
                    
            except Exception as e:
                st.error(f"An error occurred while setting up the graph: {e}")
                return

        except Exception as e:
            st.error(f"An error occurred while processing the input: {e}")
            return
