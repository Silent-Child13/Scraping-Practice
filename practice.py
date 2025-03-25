import requests
from bs4 import BeautifulSoup

url = 'https://amicares.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings:
        print(f"All Headings: {heading.text.strip()}")

    links = soup.find_all('a', href=True)
    for link in links:
        print(f"All links: {link.text.strip()}, URL: {link['href']}")

    hero_section = soup.find_all('div', class_='hero-section')
    if hero_section:
        print(f"Hero Section: {hero_section.text.strip()}")

    with open('scraped_info.txt', 'w', encoding='utf-8') as f:
        for heading in headings:
            f.write(f"All Headings: {heading.text.strip()}\n")
        for link in links:
            f.write(f"All links: {link.text.strip()}, URL: {link['href']}\n")
        if hero_section:
            f.write(f"Hero Section: {hero_section.text.strip()}\n")

    print("Specific information has been scraped successfully.")
else:
    print(f"failed to retrieve the page. Status code: {response.status_code}")
        
