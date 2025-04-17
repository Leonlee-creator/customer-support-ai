from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.agent import ask_agent

app = FastAPI()

class Question(BaseModel):
    customer_name: str
    question: str

@app.post("/ask")
def ask(question: Question):
    response = ask_agent(question.customer_name, question.question)
    return {"response": response}
