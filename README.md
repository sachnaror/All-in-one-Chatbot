---
title: All Rounder Chatbot with Memory
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.1
app_file: app.py
python_version: 3.9
pinned: false
license: apache-2.0
short_description: An intelligent chatbot with conversation memory capabilities
tags:
  - chatbot
  - ai
  - conversational-ai
  - memory
  - nlp
---
# AI Chatbot with LangGraph and Streamlit

A powerful AI chatbot application built with LangGraph, LangChain, and Streamlit that supports multiple LLM providers including Groq and OpenAI.

## 🚀 Features

- **Multi-LLM Support**: Choose between Groq and OpenAI models
- **Interactive Chat Interface**: Clean Streamlit-based chat UI
- **Persistent Chat History**: Conversations are maintained throughout the session
- **Configurable Models**: Easy model selection and configuration
- **Graph-Based Architecture**: Built with LangGraph for scalable conversation flows
- **Real-time Responses**: Streaming responses from AI models

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Framework**: LangChain + LangGraph
- **LLM Providers**:
  - Groq (Llama, Gemma models)
  - OpenAI (GPT-4o, GPT-4o-mini)
- **State Management**: LangGraph State
- **Configuration**: ConfigParser

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AI-News
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Keys**

   You have two options:

   **Option A: Environment Variables (Recommended)**
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

   **Option B: Enter in UI**
   - Leave environment variables empty
   - Enter API keys directly in the Streamlit sidebar

## 🔑 Getting API Keys

### Groq API Key
1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key

## 🚀 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the app**
   - Open your browser to `https://huggingface.co/spaces/bpratik/Chatbot`

3. **Configure the chatbot**
   - Select your preferred LLM provider (Groq or OpenAI)
   - Choose a model from the dropdown
   - Enter your API key (if not set as environment variable)
   - Select a use case

4. **Start chatting**
   - Type your message in the chat input at the bottom
   - Press Enter to send
   - View responses in the chat interface

## 📁 Project Structure

```
AI-News/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── src/
│   ├── __init__.py
│   ├── main.py                 # Core application logic
│   ├── graph/
│   │   ├── __init__.py
│   │   └── graph_builder.py    # LangGraph state graph builder
│   ├── llms/
│   │   ├── __init__.py
│   │   ├── groq.py            # Groq LLM integration
│   │   └── openai.py          # OpenAI LLM integration
│   ├── nodes/
│   │   ├── __init__.py
│   │   └── basic_chatbot.py   # Chatbot node implementation
│   ├── state/
│   │   ├── __init__.py
│   │   └── state.py           # LangGraph state definition
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── config.ini         # UI configuration
│   │   ├── config.py          # Configuration loader
│   │   ├── display_results.py # Results display component
│   │   └── load.py            # UI loader
│   ├── tools/
│   │   └── __init__.py
│   └── vectorstore/
       └── __init__.py
```

## ⚙️ Configuration

The application can be configured through `src/ui/config.ini`:

```ini
[DEFAULT]
Title = Basic Chatbot
USE_CASE = Basic Chatbot, Chatbot with Web Search
LLM_options = Groq, OpenAI
GROQ_MODEL = meta-llama/llama-4-scout-17b-16e-instruct, gemma2-9b-it, meta-llama/llama-4-maverick-17b-128e-instruct
OPENAI_MODEL = gpt-4o, gpt-4o-mini
```

## 🔧 Available Models

### Groq Models
- `meta-llama/llama-4-scout-17b-16e-instruct`
- `gemma2-9b-it`
- `meta-llama/llama-4-maverick-17b-128e-instruct`

### OpenAI Models
- `gpt-4o`
- `gpt-4o-mini`

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your API key is valid and has sufficient credits
   - Check if the API key is properly set in environment variables or entered in UI

2. **Import Errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're running from the correct directory

3. **Model Not Found**
   - Check if the model name in `config.ini` matches the provider's available models
   - Ensure your API key has access to the selected model

4. **Streamlit Issues**
   - Clear Streamlit cache: `streamlit cache clear`
   - Restart the application

### Error Messages

- **"Failed to initialize the model"**: Check API key and model availability
- **"No use case selected"**: Select a use case from the sidebar dropdown
- **"Graph must have an entrypoint"**: This indicates a configuration issue - restart the app


## 🚧 Future Enhancements

- [x] **Memory/History Implementation**: Add persistent conversation memory using LangChain's built-in memory features
- [x] **Web Search Integration**: Implement web search capabilities for the chatbot
- [ ] **File Upload Support**: Allow users to upload and chat about documents
- [ ] **Multiple Conversation Sessions**: Support for multiple concurrent chat sessions
- [ ] **Custom Model Integration**: Support for additional LLM providers
- [ ] **Chat Export**: Export conversation history to various formats

## 📩 Contact

| Name              | Details                             |
|------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                        |
| **📧 Email**       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| **📍 Location**    | Noida, India                        |
| **📂 GitHub**      | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 Phone**       | [+91 9560330483](tel:+919560330483) |

---
