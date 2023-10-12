from bs4 import BeautifulSoup
import requests

URL_BASE='https://scrapepark.org/courses/spanish/'

#obtener html
response=requests.get(URL_BASE)

html=response.text

#parsear el html
soup= BeautifulSoup(html, "html.parser")

#metodo find_all
#all_h2=soup.find_all('h2', limit=2)
all_h2=soup.find_all('h2')

for seccion in all_h2:
    print(seccion.text)

for seccion in all_h2:
    print(seccion.get_text(strip=True))





