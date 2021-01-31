import requests
from bs4 import BeautifulSoup
data=[]
import pandas as pd
import re
import os
da=[]
k="https://www.greengeeks.com/tutorials/article/top-20-git-commands-and-examples/"
page=requests.get(k)
print(page)
soup =BeautifulSoup(page.content,'html.parser')
data=[]
# print(soup.find_all('div',{'class':'hts-messages hts-messages--info    '}))
for i in soup.find_all('div',{'class':"hts-messages hts-messages--info"}):
    d=[]
    k=i.get_text().strip()
    k=k.replace('\t','')
    d.append(" ".join(k.split(" ")[:2]))
    d.append(i.previous_sibling.replace('\t',''))
    d.append(k)
    data.append(d)
for j in data:
    print(j)

    
   
df=pd.DataFrame(data,columns=["command","Description","example"])

#os.remove("data1.csv")
df.to_csv(r'github.csv',mode='a',index = False)

