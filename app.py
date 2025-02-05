import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import(
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

import streamlit as st

# Custom CSS for Chat App Styling
st.markdown("""
<style>
    /* Set Background Color */
    .main {
        background-color: #1e1e2e;
        color: #ffffff;
    }
    
    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #2a2a3a;
    }
    
    /* Chat Message Box */
    .chat-container {
        background-color: #252531;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        color: white;
    }
    
    /* User Message (Right Align) */
    .user-message {
        background-color: #3b82f6;
        text-align: right;
        padding: 8px;
        border-radius: 10px;
        color: white;
    }
    
    /* AI Message (Left Align) */
    .ai-message {
        background-color: #2d2d39;
        text-align: left;
        padding: 8px;
        border-radius: 10px;
        color: white;
    }
    
    /* Text Input Field */
    .stTextInput textarea {
        background-color: #2d2d39;
        color: white !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #3b82f6;
        color: white;
        border-radius: 5px;
    }
    
    /* Chat Scrollable Container */
    .chat-history {
        max-height: 400px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)
st.title("Chat with Ollama")
st.caption("Powered by Langchain and Ollama")

import streamlit as st

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🛠️ Debugging Assistant
    - 📄 Code Documentation
    - 🎨 Solution Design
    """)
    
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")


# Initialize ChatOllama
llm_engine=ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3,
)

# Initialize ChatPromptTemplate
system_prompt= SystemMessagePromptTemplate.from_template(
"You are an expert AI coding assistant. Provide concise, correct solutions"
"with strategic print statements for debugging. Always respond in English."

)

#session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "Hi Shanuu! I'm your coding assistant. How can I help you today?"}
    ]

#Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.write(message["content"])

#Chat input
prompt_chain=st.chat_input("Enter you coding questions here...")

def generate_response(prompt_chain):
    processing_pipeline=prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})
