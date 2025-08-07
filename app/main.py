from flask import Flask, request, jsonify

app = Flask(__name__)

words_data = {
    "serendipity": {
        "definition": "The occurrence of events by chance in a happy or beneficial way.",
        "example": "A fortunate stroke of serendipity.",
        "synonyms": ["fluke", "luck", "chance"]
    },
    "ephemeral": {
        "definition": "Lasting for a very short time.",
        "example": "Fame in the world of rock and pop is largely ephemeral.",
        "synonyms": ["transitory", "short-lived", "temporary"]
    }
}

@app.route("/define", methods=["GET"])
def define_word():
    word = request.args.get("word", "").lower()
    if word in words_data:
        return jsonify({word: words_data[word]})
    return jsonify({"error": "Word not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
