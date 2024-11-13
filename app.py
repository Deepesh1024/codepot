from flask import Flask, render_template, request, jsonify
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Initialize the ChatGroq model
llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=os.getenv("API_KEY"))

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a poet. Reply to all user queries with poetry"),
    ("user", "{query}")
])

# Store conversation history in memory
conversation_history = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Format the prompt and get the response
    formatted_prompt = prompt.format(query=user_query)
    response = llm.invoke(formatted_prompt)

    # Append to conversation history
    conversation_entry = {"query": user_query, "response": response.content}
    conversation_history.append(conversation_entry)

    # Send the updated conversation history to the frontend
    return jsonify({"response": response.content, "history": conversation_history})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5034, debug=True)

