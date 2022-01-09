from flask import Flask, jsonify

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

@app.route('/')
@app.route('/api')
@cross_origin()
def api():
    # SEE YOU ARE NOT 
    return jsonify({'data' : 'It is now working!'})

if __name__ == "__main__":
    app.run(debug=True)