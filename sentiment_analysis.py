from textblob import TextBlob

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0.5:
        return "positive"
    elif sentiment < -0.5:
        return "negative"
    else:
        return "neutral"
