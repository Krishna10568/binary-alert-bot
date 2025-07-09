
import random

def get_prediction():
    pairs = ['EUR/USD', 'GBP/JPY', 'AUD/CAD', 'USD/INR']
    action = random.choice(['BUY (↑)', 'SELL (↓)'])
    confidence = random.randint(70, 95)
    return {
        'pair': random.choice(pairs),
        'action': action,
        'confidence': confidence
    }
