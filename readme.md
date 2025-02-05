streamlit

A Python framework for building interactive web apps quickly.
Used in AI, data visualization, and machine learning dashboards.
Example:
python
Copy
Edit
import streamlit as st
st.write("Hello, Streamlit!")


langchain_core

The core module of LangChain, a framework for building applications with LLMs (Large Language Models).
Provides tools for prompt handling, memory, chains, and agents.


langchain_community

A community-supported package of LangChain.
Contains connectors for various APIs, databases, and models that aren't included in the core module.


langchain_ollama

A LangChain integration for Ollama, a tool to run LLMs locally on your machine.
Used to interact with models like DeepSeek R1, LLaMA, Mistral, etc. without cloud dependency.

app.py
import streamlit as st

Brings in Streamlit, which helps create a simple web-based user interface for the chatbot.
from langchain_ollama import ChatOllama

Imports ChatOllama, which allows the chatbot to use Ollama, a tool that runs AI models locally on your computer.
from langchain_core.output_parsers import StrOutputParser

Imports a parser that converts AI responses into readable text (instead of complex data structures).
from langchain_core.prompts import (...)

Imports different types of prompt templates:
SystemMessagePromptTemplate: Defines rules or behavior for the AI.
HumanMessagePromptTemplate: Defines how human inputs are handled.
AIMessagePromptTemplate: Defines how AI-generated responses are structured.
ChatPromptTemplate: Combines all prompts into one chat format.