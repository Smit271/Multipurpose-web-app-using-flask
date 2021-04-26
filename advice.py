import requests
import json

class Advice_API:
    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"

    def advice(self):
        res = requests.get(self.url)
        advice = res.json()
        return advice['slip']['advice']

    def __repr__(self):
        return f"Follow given advice"

