from handlers import route_intent
from intent_classifier import predict_intent

# Optional: multi-turn flag for news
awaiting_news_category = False

# 🎉 Show welcome message at start
def welcome_message():
    return (
        "Hey there! I’m your smart assistant 🤖\n"
        "I can help you with:\n"
        "• Weather info 🌤️ (e.g., What's the weather in Delhi?)\n"
        "• Stock prices 📈 (e.g., Show me Tesla stock)\n"
        "• News headlines 📰 (e.g., Tech news today)\n"
        "• Telling jokes 😄 (e.g., Tell me a joke)\n"
        "• Motivational quotes 💪 (e.g., Motivate me)\n"
        "• Flipping a coin 🪙 (e.g., Flip a coin)\n"
        "…and more!\n\n"
        "Just type your question to get started 👇\n"
    )

print("🤖 Chatbot is ready! Type 'exit' to quit.\n")
print(welcome_message())

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    if user_input == "":
        print("Bot:", welcome_message())
        continue

    # Handle news multi-turn case
    if awaiting_news_category:
        from handler_news import extract_news_category, fetch_news
        category = extract_news_category(user_input)
        if category:
            print("Bot:", fetch_news(category))
            awaiting_news_category = False
        else:
            print("Bot: Still waiting for a valid category (e.g., tech, business, sports).")
        continue

    intent = predict_intent(user_input)

    if intent == "get_news":
        from handler_news import extract_news_category, fetch_news
        category = extract_news_category(user_input)
        if category:
            print("Bot:", fetch_news(category))
        else:
            print("Bot: What kind of news are you interested in?")
            awaiting_news_category = True
        continue

    print("Bot:", route_intent(intent, user_input))
