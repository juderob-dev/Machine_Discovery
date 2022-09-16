from flask import Flask, request, jsonify
import json

app = Flask(__name__)

d = {}

@app.route('/')
def home():
    return "home"


@app.route('/scores/', methods=['POST'])
def post_scores():
    if request.is_json:
        content = request.get_json()
        name = content['name']
        score = content['score']
        if name not in d or (name in d and d[name] < score):
            d[name] = score
        return jsonify('score has been successfully added to leaderboard')
    return jsonify('Error: Request is not JSON')


@app.route('/scores/<rank>/', methods=['GET'])
def get_rank(rank):
    if rank > len(d):
        return "404 Not Found: The rank you are looking for does not exist in the leaderboard: Try decreasing the rank."
    sorted_dic = sorted(d, key=d.get, reverse=True)
    ranking = {rank:name for rank, name in enumerate(sorted_dic, 1)}
    return jsonify("name: " + key + "," + "value: " + value for key, value in d.items() if d == ranking[rank])

if __name__ =='__main__':
    app.run()
