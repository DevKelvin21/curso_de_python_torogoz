from bs4 import BeautifulSoup
import requests

#import bs4 

#print("Version de Bs4:", bs4.__version__)

#Empezar con el scraping

URL_BASE='https://scrapepark.org/courses/spanish/'

#obtener html
response=requests.get(URL_BASE)

html=response.text

#parsear el html
soup= BeautifulSoup(html, "html.parser")

#print(type(soup))

primer_h2= soup.find('h2')

print(primer_h2)