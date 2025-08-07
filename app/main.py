from flask import Flask, request, jsonify
import os

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
    },
    "resilience": {
        "definition": "The capacity to recover quickly from difficulties.",
        "example": "Her resilience was apparent after the loss.",
        "synonyms": ["toughness", "adaptability", "endurance"]
    },
    "eloquent": {
        "definition": "Fluent or persuasive in speaking or writing.",
        "example": "He gave an eloquent speech that moved the audience.",
        "synonyms": ["articulate", "expressive", "persuasive"]
    }
}

@app.route("/define", methods=["GET"])
def define_word():
    word = request.args.get("word", "").lower()
    if word in words_data:
        return jsonify({word: words_data[word]})
    return jsonify({"error": "Word not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
