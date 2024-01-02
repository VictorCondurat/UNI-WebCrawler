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

def urmareste_linkuri(start_url, tag, max_depth=5):
    visited_urls = set()
    urls_to_visit = [(start_url, 0)]
    log = []

    while urls_to_visit:
        current_url, depth = urls_to_visit.pop(0)
        if depth > max_depth:
            break

        try:
            content = obtine_continut_pagina(current_url)
            page_size = len(content)
            print(f"[DEBBUGING] Accesat {current_url}")
            log.append(f"Accesat {current_url} (Dimensiune: {page_size} bytes)")
            visited_urls.add(current_url)

            if depth < max_depth:
                soup = parseaza_html(content)
                for full_url in gaseste_linkuri(soup, tag, current_url, visited_urls):
                    urls_to_visit.append((full_url, depth + 1))
        except Exception as e:
            log.append(str(e))

    return log