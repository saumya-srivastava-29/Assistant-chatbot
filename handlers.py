import random
from transformers import pipeline
from handler_weather import handle_get_weather
from handler_stock import handle_get_stock_price
from handler_unknown import handle_unknown
from handler_news import fetch_news, extract_news_category



# Load your LLM fallback model (distilgpt2 for now)
llm = pipeline("text-generation", model="distilgpt2")

# Greeting
def handle_greeting():
    return random.choice([
        "Hey there! 👋",
        "Hi! How can I help you today?",
        "Hello, friend!"
    ])

# Goodbye
def handle_goodbye():
    return random.choice([
        "Goodbye! 👋",
        "Take care!",
        "See you again soon!"
    ])

# Thanks
def handle_thanks():
    return random.choice([
        "You're welcome! 😊",
        "No problem at all!",
        "Glad I could help!"
    ])

# Coin Flip
def handle_coin_flip():
    return f"The result is: {random.choice(['Heads', 'Tails'])}"

# Tell a Joke
def handle_tell_joke():
    return random.choice([
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why did the computer get cold? Because it left its Windows open!"
    ])

# Motivational Quote
def handle_motivational_quote():
    return random.choice([
        "Believe you can and you're halfway there.",
        "Push yourself, because no one else is going to do it for you.",
        "Don’t watch the clock; do what it does. Keep going."
    ])

# Placeholder Weather Handler

# Placeholder Stock Handler
def handle_get_stock_price(user_input):
    return "📈 Stock price lookup will be added soon!"

# Placeholder News Handler
def handle_get_news(user_input):
    return "📰 I’ll give you the latest headlines in the next update!"

# LLM Fallback Handler (for unknown/open questions)
def handle_unknown(user_input):
    response = llm(user_input, max_length=100, do_sample=True)[0]['generated_text']
    return response

def route_intent(intent, user_input):
    print("DEBUG — Routing intent:", intent)
    if intent == "greeting":
        return handle_greeting()
    elif intent == "goodbye":
        return handle_goodbye()
    elif intent == "thanks":
        return handle_thanks()
    elif intent == "coin_flip":
        return handle_coin_flip()
    elif intent == "tell_joke":
        return handle_tell_joke()
    elif intent == "motivational_quote":
        return handle_motivational_quote()
    elif intent == "get_weather":
        return handle_get_weather(user_input)
    elif intent == "get_stock_price":
        return handle_get_stock_price(user_input)
    elif intent == "get_news":
        return handle_get_news(user_input)
    else:
        return handle_unknown(user_input)
