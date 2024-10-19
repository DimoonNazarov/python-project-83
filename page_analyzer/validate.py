import validators
from urllib.parse import urlparse
import requests
import http
from bs4 import BeautifulSoup


from page_analyzer.db import get_urls_by_name


def validate_url(url):
    """
    Validation and normalization for the entered URL. The URL must have a valid
    address, it is mandatory and does not exceed 255 characters.

    :param url: Site URL.
    :return: Dict of normalized url and errors if any.
    """

    error = None

    if len(url) == 0:
        error = 'zero'
    elif len(url) > 255:
        error = 'length'
    elif not validators.url(url):
        error = 'invalid'
    else:
        parsed_url = urlparse(url)
        norm_url = f'{parsed_url.scheme}://{parsed_url.netloc}'

        found = get_urls_by_name(norm_url)

        if found:
            error = 'exists'

        url = norm_url

    valid = {'url': url, 'error': error}

    return valid


def get_url_data(url):

    response = requests.get(url)
    if  response.status_code != http.HTTPStatus.OK:
        raise requests.RequestException()
    check = {"status_code": response.status_code}

    soup = BeautifulSoup(response.text, "lxml")
    h1 = soup.find("h1")
    title  = soup.find("title")
    description = soup.find('meta', attrs={'name': 'description'})

    check['h1'] = h1.text.strip() if h1 else ""
    check['title'] = title.text.strip() if title else ""
    check["description"] = description["content"].strip() if description else ""

    return check


