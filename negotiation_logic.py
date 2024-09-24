import random
from ai_model import get_response_from_ai
from sentiment_analysis import analyze_sentiment

def handle_negotiation(user_input, user_price):
    min_price = 50
    max_price = 100
    bot_offer = random.randint(min_price, max_price)

    sentiment = analyze_sentiment(user_input)
    
    if sentiment == "positive":
        bot_offer = 0.9 * max_price  # Better offer for positive sentiment
    else:
        bot_offer = random.randint(min_price, max_price)
    
    if user_price >= bot_offer:
        ai_response = get_response_from_ai(f"The customer has offered ${user_price}, and we are accepting it.")
        return ai_response
    else:
        counter_offer = bot_offer - (0.1 * bot_offer)
        ai_response = get_response_from_ai(f"The customer has offered ${user_price}, but we would like to counter with ${counter_offer}.")
        return ai_response
