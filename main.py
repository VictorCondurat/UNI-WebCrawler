import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obtine_continut_pagina(url):
    """
    Face o cerere HTTP și returnează conținutul paginii.
    """
    try:
        response = requests.get(url)
        return response.content
    except requests.RequestException as e:
        raise Exception(f"Eroare la accesarea URL-ului {url}: {e}")
    
def parseaza_html(content):
    """
    Parsează conținutul HTML și returnează un obiect BeautifulSoup.
    """
    return BeautifulSoup(content, 'html.parser')

def gaseste_linkuri(soup, tag, current_url, visited_urls):
    """
    Găsește toate linkurile care conțin tagul specificat și returnează URL-uri complete.
    """
    for link in soup.find_all('a'):
        link_url = link.get('href')
        if link_url and tag in str(link):
            full_url = urljoin(current_url, link_url)
            if full_url not in visited_urls:
                yield full_url