from bs4 import BeautifulSoup
import requests

URL_BASE='https://scrapepark.org/courses/spanish/'

#obtener html
response=requests.get(URL_BASE)

html=response.text

#parsear el html
soup= BeautifulSoup(html, "html.parser")

#utilizando atributos de las etiquetas

'''
divs=soup.find_all('div',class_="heading-container heading-center")

for div in divs:
    print(div)
    print("")
'''


all_src=soup.find_all(src=True)

for elemento in all_src:
    if elemento['src'].endswith(".jpg"):
        print(elemento)

url_imagenes=[]

for i, imagen in enumerate(all_src):
    if imagen['src'].endswith('png'):
        print(imagen['src'])
        r=requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}.png")

        with open(f'imagen_{i}.png','wb') as f:
            f.write(r.content)