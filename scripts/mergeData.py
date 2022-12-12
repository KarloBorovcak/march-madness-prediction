import pandas as pd
import os

path = './data/teamSeedsProc/'
dir_list = os.listdir(path)
df_list = []

for i,csv in enumerate(dir_list):
    df_list.append(pd.read_csv(path + csv))
    df_list[i].fillna('NA', inplace=True)


playoff = set(df_list[0].loc[df_list[0].SEED != 'NA', 'TEAM'])

for i in range(1,len(dir_list)):
    if i != 7:
        playoff.update(set(df_list[i].loc[df_list[i].SEED != 'NA', 'TEAM']))


path2 = './data/cleanTeamStats/'
dir_list2 = os.listdir(path2)
df_list2 = []

for i,csv in enumerate(dir_list2):
    df_list2.append(pd.read_csv(path2 + csv))
    df_list2[i].fillna('NA', inplace=True)

for df in df_list2:
    print(len(df.loc[df['School'].isin(playoff)]))

playoff2 = df_list2[1].loc[df_list2[1]['School'].isin(playoff), 'School']