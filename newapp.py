# from fastapi import FastAPI, HTTPException, Request
# from langchain.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
# from langserve import add_routes
# import uvicorn
# import os
# from dotenv import load_dotenv
# import logging

# # Load environment variables
# load_dotenv()

# # Initialize logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Initialize FastAPI app
# app = FastAPI(
#     title="Politician Chatbot API",
#     version="1.0",
#     description="An API for a chatbot that replies like a politician"
# )

# # Initialize the ChatGroq model
# llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=os.getenv("API_KEY"))

# # Define the prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a politician so reply to user queries as you wanna collect their support."),
#     ("user", "{query}")
# ])

# # Add routes with the model and prompt
# add_routes(
#     app,
#     prompt | llm,
#     path="/politician_reply"
# )

# # Log request and response data for debugging
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     logger.info(f"Request URL: {request.url}")
#     response = await call_next(request)
#     logger.info(f"Response status: {response.status_code}")
#     return response

# # Run the FastAPI server
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
