import requests

VALID_CATEGORIES = [
    "business", "entertainment", "general", "health", "science", "sports", "technology"
]
NEWS_API_KEY = "eae53796d79e4882a395e1e484a52ffb"
def extract_news_category(text):
    text = text.lower()
    for category in VALID_CATEGORIES:
        if category in text:
            return category
    return None

def fetch_news(category):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&pageSize=3&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        print("DEBUG — News API Response:", data)  # <-- See full API response

        if data.get("status") != "ok":
            return "⚠️ Failed to fetch news."

        articles = data.get("articles", [])
        if not articles:
            return "📰 No articles found in this category."

        headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles)]
        return "\n\n".join(headlines)

    except Exception as e:
        return f"❌ Error fetching news: {str(e)}"