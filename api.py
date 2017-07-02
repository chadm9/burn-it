from flask import Flask, request, jsonify
#sudo pip install flask-cors
from flask_cors import CORS
from nutritionix import Nutritionix
nix = Nutritionix(app_id="67a461a2", api_key="e2e3a5f32358c6197ad841f6a0bbbb0d")

app = Flask(__name__)
CORS(app)


#pizza = nix.search("pizza")
#print nix.search('big mac', results="0:1").json()
print nix.item(id="58bedf1bde25a28564cebeb9").json()


@app.route('/', methods=['GET'])

def home_page():
    return "Hello, World!"


@app.route('/hand_checker', methods=['POST'])

def hand_checker():
    # print request.form
    hand = request.form.getlist('hand[]')
    print hand
    #hand = ['1h 2h 1s 9d 13d']
    
    return jsonify({'message': 'You have %s and %s!' % (hand[0], hand[1])})

if __name__ == '__main__':
    app.run(debug=True)
