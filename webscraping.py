import requests
from bs4 import BeautifulSoup

# URL de la página que queremos raspar
url = 'https://news.ycombinator.com/'

# Realizamos la petición a la web
response = requests.get(url)

# This function search a title with a custom word
def word_in_titles(soup):
    word = input("Insert a word to search: ")
    titles = soup.find_all('span', class_='titleline')
    cont=0
    # Imprimimos los títulos encontrados
    for title in titles:
        if word.lower() in title.text.lower():
            cont += 1
            print(title.text)
    print(f"{'='*40}\n La palabra {word} ha aparecido {cont} veces.\n{'='*40}")

# Search and list every link from the web site.
def links_list(soup):
    links = soup.find_all('a', href=True)
    
    link_cont = 0
    for link  in links:
        link_cont += 1
        print(f"{link_cont} - {link['href']}")

# Verificamos que la petición se haya realizado correctamente con response.status_code == 200
if response.status_code == 200:
    # Creamos el objeto BeautifulSoup y especificamos el parser HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    word_in_titles(soup)
    links_list(soup)

else:
    print('Error en la petición:', response.status_code)