import re
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

base_url = "https://www.kijiji.ca/b-apartments-condos/ontario/apartment/page-"
url_seperator = "/c37l9004a29276001?sort=priceAsc&ad=offering&price=700__900"
dtframe = [] #it is not in the loop so it holds and appends all entries

#request with python and beautiful soup has 3 parts URL,RESPONSE AND SOUPCONTENT

for post in range(12): #to go through the first 12 pages, to get up to 500 entries
  url = base_url + str(post+1) + url_seperator  
  response = requests.get(url)
  soupcontent = BeautifulSoup(response.content, 'html.parser') #this prints out the pagesource

  houses = soupcontent.find_all('div', {'class': 'info'})
  
  #place the variable in the main loop so it gets reset every time-> housedeetsDesiredFormat
  # create new variable and assign to empty list
  housedeetsDesiredFormat=[]

  for i in houses:
    housename = i.find('div', {'class': 'title'}).get_text()
    houseprice = i.find('div', {'class': 'price'}).get_text()
    houselocation = i.find('div', {'class': 'location'}).get_text()
    housebed = i.find('div', {'class': 'details'}).get_text()


    formattedHouseName = ' '.join(housename.strip().replace("\n", "").split());
    formattedHousePrice = ' '.join(houseprice.strip("").replace("$", "").split());
    formattedHouseLocation = ' '.join(houselocation.strip().replace("\n", "").split())
    formattedHouseBed = ' '.join(housebed.strip().replace("Beds:", "").split())

    houseRecord = [formattedHouseName, formattedHousePrice, formattedHouseLocation, formattedHouseBed]
    housedeetsDesiredFormat.append(houseRecord)
       
  print('We are at ' +str(post+1))
  print(housedeetsDesiredFormat , '\n')
  dtframe.extend(housedeetsDesiredFormat)



df = pd.DataFrame(dtframe, columns=['House_Name', 'House_Price', 'House_Location', 'House_Bed'])
print(df)

df.to_csv('KijijiFinal.csv') #convert to csv

#df.House_Bed.dtype
df.dtypes #it is an object now, need to convert to an int

df['House_Price'] = df['House_Price'].astype(float) #I needed to convert to a string first, then an integer.
print(df['House_Price'])
df.House_Price.dtype


df['House_Bed'].replace('\D+','',regex=True,inplace=True) #remove and replace the strings with a space
df['House_Bed'].replace('','0',regex=True,inplace=True) #remove and replace the space with 0
df['House_Bed'] = df['House_Bed'].astype(int)
print(df['House_Bed'])
df.House_Bed.dtype

#dataframe.column.dtype: df.A.dtype (for a particular column in a dataframe)
#dataframe.dtypes: df.dtypes (for the whole dataframe)

print(df['House_Price'])
df.House_Price.dtype
print(df['House_Bed'])
df.House_Bed.dtype


plt.scatter(df.House_Price, df.House_Bed)
plt.xlabel('Prices')
plt.ylabel('Number of Beds')
plt.title('Graph showing the Prices of Houses with Beds on Kijiji Website\n')

plt.show()