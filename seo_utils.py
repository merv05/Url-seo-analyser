import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from urllib.parse import urlparse, urljoin

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(content):
    return BeautifulSoup(content, 'html.parser')

def get_word_count(text):
    words = re.findall(r'\w+', text.lower())
    return len(words), Counter(words)

def get_meta_tags(soup):
    title = soup.find('title').string if soup.find('title') else 'No title found'
    description = soup.find('meta', attrs={'name': 'description'})
    description = description['content'] if description else 'No description found'
    return title, description

def analyze_headers(soup):
    headers = {}
    for i in range(1, 7):
        headers[f'h{i}'] = len(soup.find_all(f'h{i}'))
    return headers

def analyze_images(soup):
    images = soup.find_all('img')
    total_images = len(images)
    images_with_alt = sum(1 for img in images if img.get('alt'))
    return total_images, images_with_alt

def analyze_links(soup, base_url):
    internal_links = 0
    external_links = 0
    base_domain = urlparse(base_url).netloc

    for link in soup.find_all('a', href=True):
        href = link['href']
        absolute_url = urljoin(base_url, href)
        if urlparse(absolute_url).netloc == base_domain:
            internal_links += 1
        else:
            external_links += 1

    return internal_links, external_links

def calculate_keyword_density(word_freq, word_count, top_n=10):
    return [(word, freq, freq/word_count*100) for word, freq in word_freq.most_common(top_n)]
