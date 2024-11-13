from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import streamlit as st

llm = ChatGroq(model = "llama-3.1-70b-versatile", api_key="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")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a policemen and reject the user on every query"),
        ("user", "{query}")
    ]
)
st.title("CHATBOT")
query = st.text_input("Enter a query")

if query:
    formatted_prompt = prompt.format(query= query)
    response = llm.invoke(formatted_prompt)
    st.write(response.content)
    