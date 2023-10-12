from bs4 import BeautifulSoup
import requests

URL_BASE='https://scrapepark.org/courses/spanish/'

#obtener html
response=requests.get(URL_BASE)

html=response.text

#parsear el html
soup= BeautifulSoup(html, "html.parser")

#tablas

URL_TABLA = soup.find_all('iframe')[0]['src']

request_tabla = requests.get(f'{URL_BASE}/{URL_TABLA}')

html_tabla = request_tabla.text
soup_tabla = BeautifulSoup(html_tabla, "html.parser")
soup_tabla.find('table')

productos_faltantes = soup_tabla.find_all(['th', 'td'], attrs={'style':'color: red;'})
productos_faltantes = [talle.text for talle in productos_faltantes]

#print(productos_faltantes)

divs = soup.find_all('div', class_='detail-box')
productos = []
precios = []

for div in divs:
  if (div.h6 is not None) and ('Patineta' in div.h5.text):
    producto = div.h5.get_text(strip=True)
    precio = div.h6.get_text(strip=True).replace('$', '')
    # Se puede agregar filtros
    
    print(f'producto: {producto:<16} | precio: {precio}')
    productos.append(producto)
    precios.append(precio)

