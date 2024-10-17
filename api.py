from fastapi import FastAPI
from typing import Dict, List, Union
import xml.etree.ElementTree as ET

app = FastAPI()

# Route to access all the information
@app.get("/", response_model=Dict[str, Union[str, List[str], Dict[str, List[str]]]])
async def root():
    # Load the XML file
    tree = ET.parse('scraped_data.xml')
    root = tree.getroot()

    # Extract the title and paragraphs from the XML
    title = root.find('title').text
    paragraphs = [p.text for p in root.findall('paragraph')]
    
    # Extract sections and their content
    sections = {}
    sections_element = root.find('sections')
    
    if sections_element is not None:
        for section in sections_element.findall('section'):
            section_title = section.attrib.get('title', 'Unnamed Section')
            section_paragraphs = [p.text for p in section.findall('paragraph')]
            sections[section_title] = section_paragraphs

    # Return all data as a dictionary (to be converted to JSON)
    return {
        'title': title,
        'paragraphs': paragraphs,
        'sections': sections
    }

# Route to access the scraped data from the XML file
@app.get("/api/data", response_model=Dict[str, Union[str, List[str], Dict[str, List[str]]]])
async def get_data():
    # Load the XML file
    tree = ET.parse('scraped_data.xml')
    root = tree.getroot()

    # Extract the title and paragraphs from the XML
    title = root.find('title').text
    paragraphs = [p.text for p in root.findall('paragraph')]
    
    # Extract sections and their content
    sections = {}
    sections_element = root.find('sections')
    
    if sections_element is not None:
        for section in sections_element.findall('section'):
            section_title = section.attrib.get('title', 'Unnamed Section')
            section_paragraphs = [p.text for p in section.findall('paragraph')]
            sections[section_title] = section_paragraphs

    # Return the data as a dictionary (to be converted to JSON)
    return {
        'title': title,
        'paragraphs': paragraphs,
        'sections': sections
    }

# Route to access only the title
@app.get("/api/title", response_model=Dict[str, str])
async def get_title():
    # Load the XML file
    tree = ET.parse('scraped_data.xml')
    root = tree.getroot()

    # Extract the title
    title = root.find('title').text

    # Return the title as a dictionary
    return {'title': title}

# Route to access only the paragraphs
@app.get("/api/paragraphs", response_model=Dict[str, List[str]])
async def get_paragraphs():
    # Load the XML file
    tree = ET.parse('scraped_data.xml')
    root = tree.getroot()

    # Extract the paragraphs
    paragraphs = [p.text for p in root.findall('paragraph')]

    # Return the paragraphs as a dictionary
    return {'paragraphs': paragraphs}

# Route to access sections
@app.get("/api/sections", response_model=Dict[str, List[str]])
async def get_sections():
    # Load the XML file
    tree = ET.parse('scraped_data.xml')
    root = tree.getroot()

    # Extract sections
    sections = {}
    sections_element = root.find('sections')
    
    if sections_element is not None:
        for section in sections_element.findall('section'):
            section_title = section.attrib.get('title', 'Unnamed Section')
            section_paragraphs = [p.text for p in section.findall('paragraph')]
            sections[section_title] = section_paragraphs

    # Return sections as a dictionary
    return {'sections': sections}
