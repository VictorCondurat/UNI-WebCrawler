# Documentație pentru Web Crawler

Acest document oferă o descriere detaliată a scriptului Python dezvoltat pentru a parcurge linkurile de pe pagini web bazându-se pe un tag specificat.

## Descriere Generală

Scriptul utilizează bibliotecile `requests` și `BeautifulSoup` pentru a efectua cereri HTTP și pentru a analiza conținutul HTML al paginilor web. Scopul său este de a găsi și de a parcurge linkurile care conțin un tag specificat în atributul lor `<a>`, parcurgând web-ul până la o adâncime maximă definită.

## Componente

### Importuri

1. **requests**: Folosită pentru a efectua cereri HTTP către paginile web.
2. **BeautifulSoup** din `bs4`: Utilizată pentru parsarea și manipularea conținutului HTML.
3. **urljoin** din `urllib.parse`: Ajută la construirea URL-urilor complete din fragmente de URL.

### Funcții

1. **obtine_continut_pagina(url)**:
   - Face o cerere HTTP la un URL dat și returnează conținutul paginii.
   - Gestionează erorile legate de cererile HTTP.

2. **parseaza_html(content)**:
   - Transformă conținutul HTML brut într-un obiect BeautifulSoup pentru o manipulare ușoară.

3. **gaseste_linkuri(soup, tag, current_url, visited_urls)**:
   - Caută în documentul HTML elementele `<a>` care conțin tagul specificat.
   - Returnează URL-uri complete, evitând vizitarea repetată a acelorași adrese.

4. **urmareste_linkuri(start_url, tag, max_depth)**:
   - Parcurge recursiv linkurile de pe o pagină web, începând de la un URL de start și urmărind linkurile care conțin tagul specificat.
   - Utilizează o abordare de tip breadth-first search (BFS) și menține un registru al paginilor vizitate.

### Utilizare

Scriptul începe de la un URL specificat și caută linkuri care conțin un tag anume, parcurgând paginile web până la o adâncime maximă definită.

