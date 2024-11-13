# from langchain_community.llms import Ollama 
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import streamlit as st 

llm = ChatGroq(api_key="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", model="llama-3.1-70b-versatile")
st.title("ChatBot")

prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant. Kindly respond to user queries."),
    ("user", "{query}")
])

query = st.text_input("Enter your query:")

if query:
    formatted_prompt = prompt.format(query=query)
    response = llm.invoke(formatted_prompt)
    st.write(response.content)


