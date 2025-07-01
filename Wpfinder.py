import requests from bs4 import BeautifulSoup import time

def duckduckgo_search(query, pages=10): headers = {'User-Agent': 'Mozilla/5.0'} links = []

print(f"\n\U0001f50d Searching '{query}' WhatsApp groups...")

for page in range(pages):
    params = {
        'q': f'{query} site:chat.whatsapp.com',
        's': str(page * 50),
    }
    res = requests.get("https://html.duckduckgo.com/html/", params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    for a in soup.find_all('a', href=True):
        href = a['href']
        if "chat.whatsapp.com" in href and href not in links:
            links.append(href)

    time.sleep(1)  # Respectful crawling

if links:
    print(f"\n\u2705 Found {len(links)} group links:\n")
    for link in links:
        print("\ud83d\udd17", link)
else:
    print("\n\u274c No public WhatsApp groups found for that topic.")

=== START ===

topic = input("\n\U0001f4d8 Enter group topic (e.g. PUBG, Girls, Study, Crypto): ") duckduckgo_search(topic, pages=10)

