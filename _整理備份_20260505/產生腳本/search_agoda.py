import urllib.request
import urllib.parse
import json
import re

hotels = [
    "Richmond Hotel Obihiro Ekimae",
    "Dormy Inn Obihiro",
    "New Akan Hotel",
    "Akan Yuku no Sato Tsuruga",
    "Shiretoko Village",
    "Dormy Inn Abashiri",
    "Hotel Abashirikoso",
    "Choyo Tei Hotel",
    "Sounkyo Kanko Hotel"
]

def search_duckduckgo(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query + ' agoda')}"
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        links = re.findall(r'href="(https?://[^"]*agoda\.com[^"]*)"', html)
        for link in links:
            # DuckDuckGo sometimes redirects, so decode URL
            match = re.search(r'uddg=(https?://[^&]*)', link)
            if match:
                link = urllib.parse.unquote(match.group(1))
            
            if 'agoda.com' in link and '/hotel/' in link:
                # clean up query params
                link = link.split('?')[0]
                return link
    except Exception as e:
        print(e)
    return None

for h in hotels:
    link = search_duckduckgo(h)
    print(f"{h}: {link}")

