Personal Assistant Chatbot

An intelligent chatbot that understands user intent and responds with relevant answers using custom handlers and a fallback LLM.

This chatbot classifies user queries into predefined intents like weather, stock prices, news, jokes, and motivational quotes. If the intent is unknown, it uses an LLM (DistilGPT-2) to generate a response. It also connects to real-time APIs for live data to give the data for weather, stock prices and News.

Tools & Tech Used
- **Python** for core logic and routing
- **Streamlit** for the frontend interface
- **Scikit-learn** for intent classification
- **Hugging Face Transformers** (DistilGPT-2) for LLM fallback
- **spaCy** for named entity recognition (weather)
- **APIs**: OpenWeatherMap, News API, Yahoo Finance
