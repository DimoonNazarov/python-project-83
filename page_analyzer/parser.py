
from bs4 import BeautifulSoup


def get_url_data(content):
    data = {
        'h1': '',
        'title': '',
        'description': '',
    }
    soup = BeautifulSoup(content, "lxml")
    if soup.find("h1"):
        data["h1"] = soup.find("h1").text.strip()
    if soup.find("title"):
        data['title'] = soup.find("title").text.strip()
    meta_tag = soup.find('meta', attrs={'name': 'description'})
    if meta_tag:
        data['description'] = meta_tag['content']
    return data



