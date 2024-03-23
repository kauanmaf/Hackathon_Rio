import pandas as pd
from quart import Quart, jsonify
from quart_cors import cors

app = Quart(__name__)
app = cors(app)

@app.route("/teste")
def testando():
	iris = pd.read_csv("Iris.csv")
	dict_iris = iris.to_dict()
	return jsonify(dict_iris)