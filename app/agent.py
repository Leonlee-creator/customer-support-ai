# app/agent.py

from orders import orders
from prompts import SYSTEM_PROMPT
import openai

def find_order_info(question):
    question = question.lower()
    for order in orders:
        if order['order_id'].lower() in question or order['customer_name'].lower() in question:
            return f"Order {order['order_id']} for {order['customer_name']} is currently '{order['status']}'."
    return "Sorry, I couldn't find any order matching your details. Please double-check your Order ID or Name."

def ask_agent(question):
    # Restrict agent to only order-related questions
    keywords = ["order", "orders", "delivery", "shipping", "status"]
    if not any(word in question.lower() for word in keywords):
        return "I'm only trained to help you with order-related questions. Please ask about your order."
    
    order_info = find_order_info(question)
    
    return order_info
