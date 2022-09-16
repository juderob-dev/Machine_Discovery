from flask import Flask, request, jsonify
import json

app = Flask(__name__)

d = {}
data = {}

"""with open('scores.pickle', 'wb') as handle:
    pickle.dump(dict, handle)

with open('scores.pickle', 'rb') as handle:
    d = pickle.load(handle)"""

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
            d.update({name:score})
        return jsonify("Your score has been successfully added")
    return jsonify('Error: Request is not JSON')


@app.route('/scores/<rank>/', methods=['GET'])
def get_rank(rank):
    rank = int(rank)
    if rank > len(d) or rank < 1:
        return "404 Not Found: The rank you are looking for does not exist in the leaderboard."
    sorted_dic = sorted(d, key=d.get, reverse=True)
    ranking = {rank:name for rank, name in enumerate(sorted_dic, 1)}
    filtered = {key:value for key, value in d.items() if key == ranking[rank]}
    key,value = list(filtered.items())[0]
    data['name'] = key
    data['score'] = value
    return json.dumps(data)

if __name__ =='__main__':
    app.run()
