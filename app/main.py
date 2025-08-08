from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/define')
def define_word():
    word = request.args.get('word')
    if not word:
        return jsonify({"error": "Please provide a word"}), 400

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Word not found"}), 404

    data = response.json()

    try:
        first = data[0]
        meaning = first['meanings'][0]['definitions'][0]

        definition = meaning.get('definition')
        example = meaning.get('example', 'No example available')
        synonyms = meaning.get('synonyms')
        if not synonyms:
            synonyms = ["No synonyms available"]

        result = {
            word: {
                "definition": definition,
                "example": example,
                "synonyms": synonyms
            }
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": "Unable to parse response"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
