from flask import Flask, request, jsonify
import requests

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
        synonyms = meaning.get('synonyms', [])

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
    app.run(debug=True)
