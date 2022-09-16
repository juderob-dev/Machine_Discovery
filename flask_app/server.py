from flask import Flask, request
import json

app = Flask(__name__)

d = {}

@app.route('/')
def home():
    return "home"


@app.route('/socres/', methods=['POST'])
def post_scores():
    pass


