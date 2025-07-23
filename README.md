
# 🤖 All Rounder Chatbot with Memory


![AI Chat](https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif)

Welcome to the **All-Rounder Chatbot**: a Streamlit-powered conversational ninja ⚔️ that remembers what you said, switches LLM brains on demand, and never ghosted anyone (unlike your ex).

---

## 🌟 Why You'll Love It

- 🧠 **Has Memory** – Remembers what you said 3 messages ago (even if you forgot).
- 🧙‍♂️ **Supports Multiple LLM Wizards** – GPT-4o? ✅ Groq's Llama? ✅ Mood swings? ❌
- 🖼️ **Sleek UI** – Clean Streamlit interface that doesn't make your eyes bleed.
- ⚙️ **Customizable AF** – Bring your own models, keys, and flair.
- 🕸️ **Graph Brain** – LangGraph makes the convo flow smoother than butter on a dosa.
- ⚡ **Real-Time Replies** – Because ain't nobody got time for buffering.

---

## 🧰 Tech Ingredients (100% Organic)

| Layer         | Magic Used                        |
|---------------|-----------------------------------|
| UI            | Streamlit                         |
| Brains        | LangChain + LangGraph             |
| LLM Providers | 🧠 OpenAI, 🐴 Groq (Llama, Gemma)   |
| State         | LangGraph Memory Nodes            |
| Settings      | Good ol' ConfigParser             |

---

## 🧪 How to Bring it to Life (Install It)

```bash
git clone <your-repo-url>
cd AI-News
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

---

## 🔐 API Keys (Not the Door-to-Mordor Keys)

```bash
# Option A: Use Env Vars
export GROQ_API_KEY="your_groq_key"
export OPENAI_API_KEY="your_openai_key"
```

Or...

🎛️ Enter them manually in the sidebar like a brave warrior.

---

## 🚀 Launch Sequence

```bash
streamlit run app.py
```

Visit: [https://huggingface.co/spaces/bpratik/Chatbot](https://huggingface.co/spaces/bpratik/Chatbot)
Wave at your chatbot. It waves back (emotionally).

---

## 🧱 Folder Feng Shui

```
AI-News/
├── app.py
├── requirements.txt
└── src/
    ├── graph/
    ├── llms/
    ├── nodes/
    ├── state/
    ├── ui/
    ├── tools/
    └── vectorstore/
```

A Marie-Kondo’d repo that sparks joy ✨

---

## 🧠 Supported Models

### 🐴 Groq
- Llama 4 Scout
- Gemma2-9B
- Llama 4 Maverick

### 🧠 OpenAI
- GPT-4o
- GPT-4o-mini (when you're on a budget)

---

## 🐛 When It All Goes Wrong

- **API Key Not Working** – Is it expired or cursed? Check it.
- **Model Missing** – You sure it’s spelled right?
- **Streamlit Caching Issues** – Try:
  ```bash
  streamlit cache clear
  ```

---

## 🧙‍♂️ Roadmap to Glory

- ✅ Memory Storage
- ✅ Web Search Integration
- ⏳ File Upload
- ⏳ Multiple Chat Sessions
- ⏳ Model Plug-n-Play
- ⏳ Chat Export to PDF/Markdown/Universe

---

## 💌 Contact The Wizard Behind the Curtain

| Field       | Details                                          |
|-------------|--------------------------------------------------|
| Dev         | **Sachin Arora** 🧑‍💻                             |
| Email       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| Location    | Noida, India 🇮🇳                                 |
| GitHub      | [github.com/sachnaror](https://github.com/sachnaror) |
| Website     | [about.me/sachin-arora](https://about.me/sachin-arora) |
| Phone       | [+91 9560330483](tel:+919560330483)             |

---

> _Made with Python, passion, and a pinch of sarcasm._

![Bye Robot](https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif)
