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