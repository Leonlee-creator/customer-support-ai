# customer-support-ai

This is a customer support assistant powered by OpenAI that helps users in real-time.

# Customer Support AI Agent 🤖📦

This project is a custom-built AI customer support agent that only answers order-related queries. Built using Streamlit and OpenAI, it simulates a real-time assistant for businesses with a simple and visually appealing front end.

## 💡 Features
- Responds only to order-related questions
- Uses a custom table of customer orders
- Built with modular design for easy LLM switching
- Styled with beautiful UI and custom branding (logo included)

## 🧠 Technologies Used
- Python
- OpenAI GPT (plug-and-play model)
- Streamlit
- Pandas

## 🗃️ Project Structure
customer-support-ai/ │ ├── app/ │ ├── streamlit_app.py # Main Streamlit UI │ ├── agent.py # Handles LLM logic │ ├── prompts.py # Prompt template for agent │ └── orders.py # Fake order data for testing │ ├── .venv/ # Python virtual environment ├── README.md # Project info ├── requirements.txt # Python dependencies └── logo.png # Custom logo


## 🖥️ Run Locally

1. Clone the repo:
```bash
git clone https://github.com/Leonlee creator/customer-support-ai.git
cd customer-support-ai

## Create a virtual environment & install packages:

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

## Start the app:
streamlit run app/streamlit_app.py
