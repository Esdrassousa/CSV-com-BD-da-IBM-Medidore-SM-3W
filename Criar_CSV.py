from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
# from ibmcloudant.cloudant_v1 import CloudantV1
import re
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import datetime as dt
import pandas as pd
import csv
serviceUsername = "apikey-v2-2i7l0qp9wwbw87vpija9mi31o7yennrevo7fd87xpz00"
servicePassword = "974d78d495165a06f9f8a753ffe33542"
# serviceURL = "https://42b86470-c6b5-4354-813b-727ba9f47dce-bluemix.cloudant.com"

serviceURL = "https://apikey-v2-2i7l0qp9wwbw87vpija9mi31o7yennrevo7fd87xpz00:974d78d495165a06f9f8a753ffe33542@42b86470-c6b5-4354-813b-727ba9f47dce-bluemix.cloudantnosqldb.appdomain.cloud"


client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = 'sm3wid11'




print (client.all_dbs())

a = client.all_dbs()
print(a[2])
my_database = client[a[2]]
print(my_database)
# server_information = client.get_server_information().get_result()
# databaseName =a[0]
# result_collection = Result(a[0]) 

result_collection = Result(a[2]) 
#print(result_collection)
result_collection = Result(my_database.all_docs, include_docs=True)
result = result_collection[1] 
result11 = result_collection['5/25/2021, 10:59:26']
r = result[0]
r = r['doc']
data = (r['data'])
seD = data.split(',')
date = datetime.strptime(seD[0], '%m/%d/%Y').date()

# print(date)
# data_em_texto = '0{}/0{}/{}'.format(date.day, date.month,
# date.year)
data_em_texto = date.strftime('%d/%m/%Y')
print(data_em_texto + seD[1])
# data_e_hora = datetime.strptime(data, '%m/%d/%Y %H:%M:%S')
# print(data_e_hora)
r = r['dados']
r=r[0]
print(r['pa'])
result11 = result_collection['5/25/2021, 00:08:00' : '5/25/2021, 23:59:59' ]

    # inteiros = re.sub('[^0-9]', '', separaCorrente)
    # separaCorrenteInt  =int(inteiros)/100
    # corrente.append(separaCorrenteInt)
    # datas.append(datasSetadas)
with open('dados_Equipamento_Id_11.csv', 'w', newline='') as file:
    writer = csv.writer(file,delimiter=";")
    # fieldnames = ["pa", "pb", "pc"]
    # writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow(["Data", "Potência Ativa fase A", "Potência Ativa fase B"
                     ,"Potência Ativa fase C", "Potência Ativa Total",
                     "Potência Reativa fase A","Potência Reativa fase B", 
                     "Potência Reativa fase C","Potência Reativa Total",
                     "Potência Aparente fase A","Potência Aparente fase B",
                     "Potência Aparente fase C", "Potência Aparente Total",
                     "Tensão fase A","Tensão fase B","Tensão fase C",
                     "Corrente fase A","Corrente fase B","Corrente fase C",
                     "Corrente Total","Fator de Potência Fase A",
                     "Fator de Potência Fase B","Fator de Potência Fase C",
                     "Fator de Potência Total"])
    for  i in range(len(result11)):
        separadados = result11[i]
        separaemDoc = separadados['doc']
        
        separaDadosDoc = separaemDoc['dados']
        Pega_primeiro_separaDadosDoc = separaDadosDoc[0]
        PotAti_A = Pega_primeiro_separaDadosDoc['pa'].replace('.',',')
        PotAti_B = Pega_primeiro_separaDadosDoc['pb'].replace('.',',')
        PotAti_C = Pega_primeiro_separaDadosDoc['pc'].replace('.',',')
        PotAti_T = Pega_primeiro_separaDadosDoc['pt'].replace('.',',')
        PotRea_A = Pega_primeiro_separaDadosDoc['qa'].replace('.',',')
        PotRea_B = Pega_primeiro_separaDadosDoc['qb'].replace('.',',')
        PotRea_C = Pega_primeiro_separaDadosDoc['qc'].replace('.',',')
        PotRea_T = Pega_primeiro_separaDadosDoc['qt'].replace('.',',')
        PotApa_A = Pega_primeiro_separaDadosDoc['sa'].replace('.',',')
        PotApa_B = Pega_primeiro_separaDadosDoc['sb'].replace('.',',')
        PotApa_C = Pega_primeiro_separaDadosDoc['sc'].replace('.',',')
        PotApa_T = Pega_primeiro_separaDadosDoc['st'].replace('.',',')
        TenFase_A = Pega_primeiro_separaDadosDoc['uarms'].replace('.',',')
        TenFase_B = Pega_primeiro_separaDadosDoc['ubrms'].replace('.',',')
        TenFase_C = Pega_primeiro_separaDadosDoc['ucrms'].replace('.',',')
        CorreFase_A = Pega_primeiro_separaDadosDoc['iarms'].replace('.',',')
        CorreFase_B = Pega_primeiro_separaDadosDoc['ibrms'].replace('.',',')
        CorreFase_C = Pega_primeiro_separaDadosDoc['icrms'].replace('.',',')
        CorreFase_T = Pega_primeiro_separaDadosDoc['itrms'].replace('.',',')
        FP_A = Pega_primeiro_separaDadosDoc['pfa'].replace('.',',')
        FP_B = Pega_primeiro_separaDadosDoc['pfb'].replace('.',',')
        FP_C = Pega_primeiro_separaDadosDoc['pfc'].replace('.',',')
        FP_T = Pega_primeiro_separaDadosDoc['pft'].replace('.',',')
        separaDatas = separaemDoc['data']
        separraData_e_Horas = separaDatas.split(',')
        date = datetime.strptime(separraData_e_Horas[0], '%m/%d/%Y').date()
        data_em_texto = date.strftime('%d/%m/%Y')
        datasSetadas = pd.to_datetime(separaDatas)
        writer.writerow([(data_em_texto+separraData_e_Horas[1]),
                         PotAti_A, PotAti_B, PotAti_C,PotAti_T,
                         PotRea_A, PotRea_B, PotRea_C,PotRea_T,
                         PotApa_A,PotApa_B,PotApa_C,PotApa_T,
                         TenFase_A,TenFase_B,TenFase_C,
                         CorreFase_A,CorreFase_B,CorreFase_C,CorreFase_T,
                         FP_A,FP_B,FP_C,FP_T])
    # writer.writerow([r['pa'],r['pb'],r['pc']])
    # writer.writerow([r['pa'],r['pb'],r['pc']])
# print(r['dado'])
