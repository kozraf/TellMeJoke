from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import mysql.connector

# Database connection details
db_host = "database-tier-service"
db_port = 3306
db_user = "root"
db_password = "mysecretpassword"
db_name = "jokes_db"  # Update with the actual database name

app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route('/getJoke')
def get_joke():
    # Retrieve a random joke from the MySQL database
    conn = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT joke, words, letters, sentences FROM jokes ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return jsonify({'joke': result[0], 'words': result[1], 'letters': result[2], 'sentences': result[3]})
    else:
        return jsonify({'joke': 'No jokes found'})


@app.route('/addJoke', methods=['POST'])
def add_joke():
    joke = request.json.get('joke')
    if joke:
        # Insert the joke into the MySQL database
        conn = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conn.cursor()

        # Calculate joke stats
        words_count = len(joke.split())
        letters_count = len(joke) - joke.count(' ')
        sentences_count = joke.count('.') + joke.count('!') + joke.count('?')

        # Insert the joke and its stats into the database
        cursor.execute("INSERT INTO jokes (joke, words, letters, sentences) VALUES (%s, %s, %s, %s)",
                       (joke, words_count, letters_count, sentences_count))

        conn.commit()
        cursor.close()
        conn.close()
        return {'message': 'Joke added!'}
    else:
        return {'message': 'No joke provided.'}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
