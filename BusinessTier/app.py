from flask import Flask, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the chicken go to the seance? To talk to the other side!",
    "Why don't some animals play cards? Because they're afraid of cheetahs!"
]

@app.route('/getJoke')
def get_joke():
    return {
        'joke': random.choice(jokes),
        'words': len(jokes[0].split()),
        'letters': len(jokes[0].replace(" ", "")),
        'sentences': len(jokes[0].split("."))
    }

@app.route('/addJoke', methods=['POST'])
def add_joke():
    joke = request.json.get('joke')
    if joke:
        jokes.append(joke)
        return {'message': 'Joke added!'}
    else:
        return {'message': 'No joke provided.'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
