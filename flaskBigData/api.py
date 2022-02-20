from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/consulta1/')
def hello_world():  # put application's code here
    global path
    data = pd.read_csv(path)
    data = data.to_dict('records')
    return {'data': data}, 200
if __name__ == '__main__':
    app.run(debug=True)