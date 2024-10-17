import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# URL of the Wikipedia page
url = 'https://ro.wikipedia.org/wiki/Regele_Arthur'

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the page
title = soup.find('h1', class_='firstHeading').text.strip()

# Extract the first three paragraphs from the page
paragraphs = soup.find_all('p')[:3]

# Extract sections (headers) and their corresponding content
sections = {}
for header in soup.find_all(['h2', 'h3']):
    section_title = header.text.strip()
    # Get the next sibling until the next header
    content = []
    for sibling in header.find_next_siblings():
        if sibling.name in ['h2', 'h3']:  # Stop at the next header
            break
        if sibling.name == 'p':  # Only consider paragraphs
            content.append(sibling.text.strip())
    sections[section_title] = content

# Collect data into a dictionary
scraped_data = {
    'title': title,
    'paragraphs': [p.text.strip() for p in paragraphs],
    'sections': sections
}

# Print the scraped data (for checking)
print(f"Title: {scraped_data['title']}")
for i, paragraph in enumerate(scraped_data['paragraphs'], 1):
    print(f"Paragraph {i}: {paragraph}")
for section, content in scraped_data['sections'].items():
    print(f"Section: {section}")
    for paragraph in content:
        print(f" - {paragraph}")

# Create the XML structure
root = ET.Element('scrapedData')

# Add title to the XML
title_element = ET.SubElement(root, 'title')
title_element.text = scraped_data['title']

# Add paragraphs to the XML
for i, paragraph in enumerate(scraped_data['paragraphs'], 1):
    p_element = ET.SubElement(root, 'paragraph', id=str(i))
    p_element.text = paragraph

# Add sections to the XML
sections_element = ET.SubElement(root, 'sections')
for section, content in scraped_data['sections'].items():
    section_element = ET.SubElement(sections_element, 'section', title=section)
    for paragraph in content:
        p_element = ET.SubElement(section_element, 'paragraph')
        p_element.text = paragraph

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the XML data to a file
tree.write('scraped_data.xml')

print("Data saved to scraped_data.xml")
