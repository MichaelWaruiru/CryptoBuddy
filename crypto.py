"""
CryptoBuddy: First AI-Powered Fiancial Sidekick which is a rule-based cryptocurrency advisor chatbot!
"""

BOT_NAME = "CryptoBuddy"
BOT_TONE = "Friendly, helpful, and a bit meme-loving."

DISCLAIMER = "Crypto is risky. Always do your own research!"

# Predefined Crypto data
crypto_db = {
  "Bitcoin": {
    "price_trend": "rising",
    "market_cap": "high",
    "energy_use": "high",
    "sustainability_score": 0.3
  },
  "Ethereum": {
     "price_trend": "stable",  
      "market_cap": "high",  
      "energy_use": "medium",  
      "sustainability_score": 0.6  
  },
  "Cardano": {  
    "price_trend": "rising",  
    "market_cap": "medium",  
    "energy_use": "low",  
    "sustainability_score": 0.8
  }   
}

# Chatbot logic and advice rules
def get_most_sustainable():
  # Highest sustainability_score and low energy use
  sustainable = [
    (name, data) for name, data in crypto_db.items()
    if data["energy_use"] == "low" and data["sustainability_score"] > 0.7
  ]
  if sustainable:
    coin = max(sustainable, key=lambda x: x[1]["sustainability_score"])[0]
    print(f"Invest in {coin}! 🌱 It’s eco-friendly and has long-term potential!")
  # Fallback: Has the highest score
  coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
  return f"{coin} has the highest sustainability score! 🌱"

def get_trending_up():
  coins = [name for name, d in crypto_db.items() if d["price_trend"] == "rising"]
  if coins:
      return f"These cryptos are trending up: {', '.join(coins)}"
  return "None of the tracked cryptos are currently trending up."

def get_profitable():
  candidates = [
    (name, data) for name, data in crypto_db.items()
    if data["price_trend"] == "rising" and data["market_cap"] == "high"
  ]
  if candidates:
    coin = candidates[0][0]
    return f"{coin} is rising and has a high market cap—looks profitable! 💰"
  return "No coin fits the classic 'profitable' profile right now."

def get_recommendation_for_long_term():
  # Prioritize rising, sustainability_score > 7/10, and energy_use low
  for name, data in crypto_db.items():
    if (
        data["price_trend"] == "rising"
        and data["sustainability_score"] > 0.7
        and data["energy_use"] == "low"
    ):
        return f"{name} is trending up and has a top-tier sustainability score!"
  return "No clear winner for long-term growth at the moment."

def handle_query(user_query):
  query = user_query.lower()
  if "sustainable" in query or "eco" in query or "green" in query:
      return get_most_sustainable()
  elif "trending" in query or "up" in query:
      return get_trending_up()
  elif "profitable" in query or "profit" in query:
      return get_profitable()
  elif "long-term" in query or "growth" in query or "future" in query:
      return get_recommendation_for_long_term()
  elif "bitcoin" in query:
      data = crypto_db["Bitcoin"]
      return f"Bitcoin is {data['price_trend']} with high market cap, but its sustainability score is low ({data['sustainability_score']*10}/10)."
  elif "ethereum" in query:
      data = crypto_db["Ethereum"]
      return f"Ethereum is {data['price_trend']} with high market cap and moderate sustainability ({data['sustainability_score']*10}/10)."
  elif "cardano" in query:
      data = crypto_db["Cardano"]
      return f"Cardano is {data['price_trend']} with medium market cap, low energy use, and a strong sustainability score ({data['sustainability_score']*10}/10)."
  elif "help" in query or "advice" in query:
      return "Ask me about trending, sustainable, or profitable cryptos! Example: 'Which crypto is trending up?'"
  else:
      return "Sorry, I didn't get that! Try asking about sustainable, trending, or profitable coins."

# Test Chatbot(Sample Conversation)
def chat():
  print(f"{BOT_NAME}: Hey there! I'm your AI-powered crypto sidekick. {BOT_TONE}\n")
  print(f"{BOT_NAME}: Type your question (type 'exit' to quit).")
  while True:
      user = input("You: ")
      if user.strip().lower() in ["exit", "quit"]:
          print(f"{BOT_NAME}: See you soon! {DISCLAIMER}")
          break
      response = handle_query(user)
      print(f"{BOT_NAME}: {response}")
      print(f"{BOT_NAME}: {DISCLAIMER}\n")

if __name__ == "__main__":
  chat()