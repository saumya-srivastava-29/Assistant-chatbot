import joblib
import streamlit as st
from handlers import route_intent
from intent_classifier import predict_intent
from handler_news import fetch_news
from handler_stock import handle_get_stock_price
from nlp_utils import get_nlp



# Load model
model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_intent(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]

# Set up page
st.set_page_config(page_title="LLM Chatbot", layout="centered")
st.title("🤖 LLM-Powered Chatbot")

st.markdown(
    "Hi! I'm your smart assistant. I can help you with:\n"
    "- 🌤️ Weather\n"
    "- 📈 Stock prices\n"
    "- 📰 News\n"
    "- 😄 Jokes\n"
    "- 💪 Motivation\n"
    "- 🪙 Flip a coin\n"
    "\nType your question below to get started 👇"
)

# Dropdown options for news and stocks
NEWS_CATEGORIES = {
    "Technology 🖥️": "technology",
    "Business 💼": "business",
    "Sports ⚽": "sports",
    "Health 🏥": "health",
    "Science 🔬": "science",
    "Entertainment 🎬": "entertainment",
    "General 🌐": "general"
}

STOCK_OPTIONS = {
    "Apple (AAPL) 🍏": "AAPL",
    "Tesla (TSLA) 🚗": "TSLA",
    "Microsoft (MSFT) 💻": "MSFT",
    "Amazon (AMZN) 📦": "AMZN",
    "Google (GOOGL) 🔍": "GOOGL"
}

# 🧠 Input form with Send button and auto-clear
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="input", placeholder="Ask me something...")
    submitted = st.form_submit_button("Send")

# If user hits Send
if submitted and user_input:
    intent = predict_intent(user_input)

    # ✅ News intent with dropdown
    if intent == "get_news":
        st.markdown("🗞️ What kind of news are you interested in?")
        selected_category = st.selectbox("Choose a news category:", options=list(NEWS_CATEGORIES.keys()))
        if selected_category:
            category = NEWS_CATEGORIES[selected_category]
            response = fetch_news(category)
            st.write("Bot:", response)

    # ✅ Stock intent with dropdown
    elif intent == "get_stock_price":
        st.markdown("📈 Which stock would you like to check?")
        selected_stock = st.selectbox("Choose a stock:", options=list(STOCK_OPTIONS.keys()))
        if selected_stock:
            ticker = STOCK_OPTIONS[selected_stock]
            response = handle_get_stock_price(ticker)
            st.write("Bot:", response)

    # ✅ All other intents
    else:
        response = route_intent(intent, user_input)
        st.write("Bot:", response)


