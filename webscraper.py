import pandas as pd
import requests
from bs4 import BeautifulSoup

#request with python and beautiful soup has 3 parts URL,RESPONSE AND SOUPCONTENT
url = 'https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XfuLN2RKjDc' #website we want to scrape
response = requests.get(url)
soupcontent = BeautifulSoup(response.content, 'html.parser') #this prints out the pagesource

week = soupcontent.find(id='seven-day-forecast-body')
items = week.find_all(class_= 'tombstone-container')
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

periodname = [item.find(class_='period-name').get_text() for item in items]#list comprehension using a for-loop to loop over the list in the weather of each days
shortdescription = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]#list compr

print(periodname)
print(shortdescription)
#print(temperature)

#Put in a Dictionary using DataFrame, using period column, shortdesc column and temp column
weather = pd.DataFrame({
  'Period': periodname,
  'Shortdescription': shortdescription,
  'Temperature': temperature
})
print(weather)

#weather.to_csv('weatherfile.csv') #convert to csv file, SO FREAKING COOL !!!
#res.to_excel('new.xlsx', sheet_name='Page_2', columns= ['Detail','Price','Time'], index = False)

