from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def compound_sentiment_score(self, s: str):
        return self.sia.polarity_scores(s)['compound']
