import requests
from bs4 import BeautifulSoup
import json


def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(
            f"Error fetching data from {url}. Status code: {response.status_code}")


def extract_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Fetch all <p> elements
    p_elements = soup.find_all('p')

    # Fetch all <a> elements (anchors)
    a_elements = soup.find_all('a')

    # Extract text content from elements
    p_texts = [p.get_text() for p in p_elements]
    a_links = [a.get('href') for a in a_elements]

    return p_texts, a_links


def save_data_to_json(url, paragraphs, anchors):
    data = {
        'url': url,
        'paragraphs': paragraphs,
        'anchors': anchors
    }
    file_name = f'{url.replace("://", "_").replace("/", "_")}.json'
    with open(f"data/{file_name}", 'w') as json_file:
        json.dump(data, json_file, indent=4)
