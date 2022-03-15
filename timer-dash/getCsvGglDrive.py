
import pandas as pd
#STORAGE DRIVE: URL OF DATA FILE: https://drive.google.com/drive/folders/1pAuUN-h_iJyw33a85F57Kow5KvXvXEtl


#Dedicated time
url_DT = 'https://drive.google.com/file/d/1Dig40yP0swJMsYWvtXOQFnwnayEi6Lvx/view?usp=sharing'
#Upcoming events
url_UE = 'https://drive.google.com/file/d/1fO0-X1ImngZVF1AoBCpFdHJdzsnutdmL/view?usp=sharing'
#Week advancement
url_WA = 'https://drive.google.com/file/d/12195l299XJRsRYCpZ1FS1wGZTngHNeBE/view?usp=sharing'


def convert2df(url):
    path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    df = pd.read_csv(path)
    return df

df_DedicatedTime = convert2df(url_DT)
print(df_DedicatedTime)

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def save2drive(df):
    # drive.mount('drive/My Drive')
    # path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
    # df.to_csv("multitasking_app\data.csv")
    # #df.to_csv('data.csv')
    # os.system('!cp data.csv "drive/My Drive/"')
    # # df = pd.read_csv(path)
    # # if df.empty:
    # #     print('empty')
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    df.to_csv('data.csv')
    df_list = 'data.csv'
    path = '/home/txa/Documents/DashBeginnerTutorials/'
    #for upload_file in df_list:
    gfile = drive.CreateFile({'parents': [{'id': '1BamlPOPoPZrdzwJGYyH68LTwyI6Sxvr8'}]})
    gfile.SetContentFile(os.path.join(path, df_list))
    #os.path.join(path, df_list)
    #gfile.SetContentFile(df_list)
    gfile.Upload()
    gfile = None

#save2drive(df_DedicatedTime)

df_DedicatedTime= df_DedicatedTime.drop('Nb exercise routines', axis = 1)
print(df_DedicatedTime)