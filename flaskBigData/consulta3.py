import pandas as pd
import os
import time

start = time.time()
df = pd.DataFrame()
nameFinalFile="csvsprocesados/consulta3_hasta2008.csv"
archivos=os.listdir("./csvs")
#decomentar las siguientes 2 lineas para generar los datos solo hasta 2007
# archivos.pop()#para no tomar en cuenta el ultimo csv en este caso el 2008
# nameFinalFile="csvsprocesados/consulta3_hasta2007.csv"
for filename in archivos:
    print(filename)
    speedlayerview = pd.read_csv("./csvs/" + filename, encoding="windows-1251")
    vistaatrasosRdes = speedlayerview.groupby(['Origin', 'Dest']).agg(
        {"CarrierDelay": tuple}).reset_index()  # retrasos llegada
    vistaatrasosRdes["retrasosLlegada"] = vistaatrasosRdes['CarrierDelay'].apply(lambda x: len([i for i in x if i > 0]))
    vistaatrasosRorg = speedlayerview.groupby(['Origin', 'Dest']).agg(
        {"WeatherDelay": tuple}).reset_index()  # retrasos salida
    vistaatrasosRorg["rorg"] = vistaatrasosRorg['WeatherDelay'].apply(lambda x: len([i for i in x if i > 0]))
    consulta3 = vistaatrasosRorg.assign(rdes=vistaatrasosRdes["retrasosLlegada"])[["rorg", "rdes", "Origin", "Dest"]]
    print(consulta3)
    df = pd.concat([df, consulta3])
originretarases=df.groupby(['Origin', 'Dest']).agg({"rorg": tuple}).reset_index()#retrasos llegada
originretarases["rorg"]= originretarases['rorg'].apply(lambda x: sum(x))
destinretarases=df.groupby(['Origin', 'Dest']).agg({"rdes": tuple}).reset_index()#retrasos llegada
destinretarases["rdes"]= destinretarases['rdes'].apply(lambda x: sum(x))
dfFinal=originretarases.assign(rdes=destinretarases["rdes"])
dfFinal.to_csv(nameFinalFile, index=False)
print(dfFinal)
end = time.time()
print("time",end - start)
