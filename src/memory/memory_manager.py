from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class MemoryManager:
    """
    Manages chat memory for the chatbot using LangChain's built-in memory features.
    """
    
    def __init__(self):
        self.store = {}
    
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        """
        Get or create a chat message history for a given session ID.
        
        :param session_id: Unique identifier for the chat session
        :return: ChatMessageHistory instance for the session
        """
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]
    
    def create_memory_enabled_model(self, model, session_id: str = "default"):
        """
        Create a model with message history enabled.
        
        :param model: The LLM model to wrap with memory
        :param session_id: Session ID for this conversation
        :return: Model with message history
        """
        with_message_history = RunnableWithMessageHistory(
            model, 
            self.get_session_history
        )
        
        config = {"configurable": {"session_id": session_id}}
        return with_message_history, config
    
    def clear_session(self, session_id: str):
        """
        Clear the message history for a specific session.
        
        :param session_id: Session ID to clear
        """
        if session_id in self.store:
            del self.store[session_id]
    
    def get_all_sessions(self):
        """
        Get all active session IDs.
        
        :return: List of session IDs
        """
        return list(self.store.keys())
