import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

iris = pd.read_csv("Iris.csv")

@app.route("/teste")
def testando():
	dict_iris = iris.to_dict()
	return jsonify(dict_iris)