import json

from flask import Flask, render_template


app = Flask(__name__)


def load_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/academic')
def academic():
    words = load_words('glossaries/academic.json')
    title = "Академический словарь"
    return render_template('index.html', words_amount=len(words), title=title, words=words)


@app.route('/prof')
def prof():
    words = load_words('glossaries/prof.json')
    title = "Профессиональный словарь"
    return render_template('index.html', words_amount=len(words), title=title, words=words)


if __name__ == '__main__':
    app.run(debug=True)
