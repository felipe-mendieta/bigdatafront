from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/consulta1/<string:year>/')
def consulta1(year: str):
  path="csvsprocesados/consulta1_hasta"+year+".csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return {'data': data}, 200

@app.route('/consulta2/<string:year>/')
def consulta2(year: str):
  path="csvsprocesados/consulta2_hasta"+year+"join.csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return {'data': data}, 200

@app.route('/consulta3/<string:year>/')
def consulta3(year: str):
  path="csvsprocesados/consulta3_hasta"+year+"join.csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return {'data': data}, 200


if __name__ == '__main__':
    app.run(debug=True)
