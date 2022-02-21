from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app,resources={r"/*/*":{"origins":"*"},})

@app.route('/consulta1/')
def hello_world():  # put application's code here
    global path
    data = pd.read_csv("consulta1_hasta2007.csv")
    data = data.to_dict('records')
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)
