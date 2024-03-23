import logging
import pandas as pd
from quart import Quart, jsonify
from quart_cors import cors


app = Quart(__name__)
app = cors(app)


@app.get("/api/teste")
async def testando():
	iris = pd.read_csv("Iris.csv")
	dict_iris = iris.to_dict()
	return jsonify(dict_iris)

if __name__ == "__main__":
    # Configure logging

    app.run()