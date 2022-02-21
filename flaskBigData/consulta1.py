import pandas as pd
import os
import time

start = time.time()
df = pd.DataFrame()
nameFinalFile="csvsprocesados/consulta1_hasta2008.csv"
archivos=os.listdir("./csvs")
#decomentar las siguientes 2 lineas para generar los datos solo hasta 2007
# archivos.pop()#para no tomar en cuenta el ultimo csv en este caso el 2008
# archivos.pop()#para no tomar en cuenta el ultimo csv en este caso el 2008,2007
#nameFinalFile="csvsprocesados/consulta1_hasta2007.csv"
for filename in archivos:
    print(filename)
    speedlayerview = pd.read_csv("./csvs/"+filename, encoding="windows-1251")[
         ["ArrDelay", "DepDelay", "Origin", "Dest", "CarrierDelay", "WeatherDelay", "UniqueCarrier"]]
    vistaatrasosRdes = speedlayerview.groupby(['Origin', 'Dest']).agg(
        {"ArrDelay": tuple}).reset_index()  # retrasos llegada
    vistaatrasosRdes["retrasosLlegada"] = vistaatrasosRdes['ArrDelay'].apply(lambda x: len([i for i in x if i > 0]))
    vistaatrasosRorg = speedlayerview.groupby(['Origin', 'Dest']).agg(
        {"DepDelay": tuple}).reset_index()  # retrasos salida
    vistaatrasosRorg["rorg"] = vistaatrasosRorg['DepDelay'].apply(lambda x: len([i for i in x if i > 0]))
    consulta1 = vistaatrasosRorg.assign(rdes=vistaatrasosRdes["retrasosLlegada"])[["rorg", "rdes", "Origin", "Dest"]]
    print(consulta1)
    df=pd.concat([df, consulta1])

originretarases=df.groupby(['Origin', 'Dest']).agg({"rorg": tuple}).reset_index()#retrasos llegada
originretarases["rorg"]= originretarases['rorg'].apply(lambda x: sum(x))
destinretarases=df.groupby(['Origin', 'Dest']).agg({"rdes": tuple}).reset_index()#retrasos llegada
destinretarases["rdes"]= destinretarases['rdes'].apply(lambda x: sum(x))
dfFinal=originretarases.assign(rdes=destinretarases["rdes"])
#haciendo join con nombres de aeropuertos
df1 = pd.read_csv("filesforjoin/airports.csv")[["iata","airport"]]
df_res = pd.merge(dfFinal, df1, how='left', left_on="Origin", right_on="iata")
df_res = pd.merge(df_res, df1, how='left', left_on="Dest", right_on="iata")
df_res=df_res[["rorg","rdes","airport_x","airport_y"]]
df_res.rename(columns = {'airport_x':'Origin', "airport_y": "Dest"}, inplace = True)
df_res.to_csv(nameFinalFile, index=False)
print(df_res)
end = time.time()
print("time",end - start)
