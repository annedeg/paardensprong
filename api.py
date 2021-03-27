import PaardenSprong
from PaardenSprong import get_correct_word
import flask
from flask import request, jsonify
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    letters = request.args.get("letters")
    if letters:
        word = get_correct_word(list(letters))
        if word:
            return jsonify(word)
    return "No"

app.run()