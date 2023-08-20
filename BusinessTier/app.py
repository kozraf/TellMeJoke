from flask import Flask, request
from flask_cors import CORS
import random
import mysql.connector

# Database connection details
db_host = "database-tier-service"
db_port = 3306
db_user = "root"
db_password = "mysecretpassword"
db_name = "your_database_name"  # Update with the actual database name

# Function to establish a connection to the database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to close the database connection
def close_db_connection(connection):
    if connection:
        connection.close()

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
