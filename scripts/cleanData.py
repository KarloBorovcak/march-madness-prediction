import pandas as pd
import os



def clean_data(lista):
    for i,data in enumerate(lista):
        data.columns = data.iloc[0]
        data = data.iloc[1:,:]
        data = data.dropna(axis=1, how='all')

        data.columns.values[3:5] = ["Overall.W","Overall.L"]
        data.columns.values[8:10] = ["Conf.W","Conf.L"]
        data.columns.values[10:12] = ["Home.W","Home.L"]
        data.columns.values[12:14] = ["Away.W","Away.L"]
        lista[i] = data


    data = pd.merge(lista[0], lista[1], how="outer", on=list(lista[0].columns.values[:16]))
    del data[data.columns[0]]
    data.rename(columns={'Tm.':'TP','Opp.':'OP'}, inplace=True)

    data.School = data.School.apply(lambda x: x[:-5] if 'NCAA' in x else x)
  

    return data



path = './data/rawTeamStats/'
new_path = './data/cleanTeamStats/'
dir_list = os.listdir(path)
lista = []

while len(dir_list) > 0:
    if len(dir_list) == 4:
        lista = dir_list[0:]
    else:
        lista = dir_list[0:5]

    lista_df = []

    lista_df.append(pd.read_csv(path + lista[2]))
    lista_df.append(pd.read_csv(path + lista[0]))

    data_school = clean_data(lista_df[0:2])
    


    data_school.to_csv(new_path + lista[3], index=False)
    
    
    for i in range(4):
        del dir_list[0]

