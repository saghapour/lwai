from flask import Flask, request, jsonify
from modules.ner.base.BaseNER import BaseNER
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi there. I'm the AI api"

@app.before_first_request
def cache_model():
    newsfa_ner = BaseNER('news_fa')
    twitter_ner = BaseNER('twitter')
    telegram_ner = BaseNER('telegram')
    app.newsfa_ner = newsfa_ner
    app.twitter_ner = twitter_ner
    app.telegram_ner = telegram_ner

@app.route('/ner/<module>/', methods=['POST'])
def ner(module: str):
    result = {'success': True}
    
    data = request.values.get('data')
    data = json.loads(data)
    if module == 'news_fa':
        prediction = app.newsfa_ner.get(data)
        result['prediction'] = prediction

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=8088)