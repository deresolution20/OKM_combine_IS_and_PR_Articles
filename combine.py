# -*- coding: utf-8 -*-
"""OKM combine IS and PR CSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kP30hCetZZMFLovizJoY4qukqmVqKw40
"""

#Import Pandas and Numpy
import pandas as pd
import numpy as np
pd.__version__

"""get shareable link from google sheet and obtain file id using javascript in chrome (ctrl + Shift + J)

var url = "https://drive.google.com/open?id=1KTwBfALwywAdDsBRevzCX6mPI1QAWsZ8" function getIdFromUrl(url) { return url.match(/[-\w]{25,}/); } getIdFromUrl(url)


https://drive.google.com/file/d/1MzeRjN-BE22RqwtrKakTV4AxfTqtWL45/view?usp=sharing

OKM IS articles FileID="1MzeRjN-BE22RqwtrKakTV4AxfTqtWL45"

OKM PR articles FileID="1Ew39z6HJKF7R14tNMXBSo_LIe7eQ48xx"

Next Install PyDrive
"""

!pip install PyDrive

#next import modules to create connection between Colab and Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

#autheticate and create PyDrive client
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive (gauth)

#import the files from google drive
#downloaded1 = drive.CreateFile({'id':"14ico7WBF73I2YJglGK60IFXTbzzazIY5"}) ##CSV IS articles
#downloaded2 = drive.CreateFile({'id':"1nVleWndeiuoQD5LuDQ0aJXXnnBfYzRmV"}) ##CSV PR articles
downloaded1 = drive.CreateFile({'id':"1MzeRjN-BE22RqwtrKakTV4AxfTqtWL45"}) ##XLS IS articles
downloaded2 = drive.CreateFile({'id':"1Ew39z6HJKF7R14tNMXBSo_LIe7eQ48xx"}) ##XLS PR articles

downloaded1.GetContentFile('IS articles')
print('Downloaded IS articles file with ID {}'.format(downloaded1.get('id')))
downloaded2.GetContentFile('PR articles')
print('Downloaded PR articles file with ID {}'.format(downloaded2.get('id')))

#import is articles into dataframe 1
#df1=pd.read_csv('IS articles')
#print(df1)

#importing XLS file in dataframe1
df1=pd.read_excel('IS articles')
print(df1)

#import pr articles into dataframe 2
df2=pd.read_excel('PR articles')
print(df2)
#df2=pd.read_csv('PR articles')

#new data frame to combine the two data frames
all_df_list=[df1,df2]

#combining the data frames into one
appended_df=pd.concat(all_df_list)

#test results to verify
print(appended_df)

#Converting merged workbook into xlsx

appended_df.to_excel("Combined IS and PR articles.xlsx", index=False)  ##Index=false removes the index added by pandas


#appended_df.to_csv("Combined IS and PR articles.csv", index=False)  ##creating csv
#testing download
##from google.colab import files
##files.download('Combined IS and PR articles.xlsx')

uploaded=drive.CreateFile({'Combined IS and PR articles.xlsx': 'Combined IS and PR articles.xlsx'})
uploaded.SetContentFile('Combined IS and PR articles.xlsx')
uploaded.Upload()
print('Uploaded file with ID {}'.format(uploaded.get('id')))
