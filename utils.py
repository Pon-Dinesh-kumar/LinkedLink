# utils.py
import requests
from bs4 import BeautifulSoup
from config import COOKIES, HEADERS

def get_profile_url(user_id):
    """
    Constructs the LinkedIn profile URL for the given user ID.
    """
    return f'https://www.linkedin.com/in/{user_id}/'

def scrape_profile(user_id):
    """
    Scrapes the LinkedIn profile for the given user ID and extracts links and email addresses.
    """
    url = get_profile_url(user_id)
    response = requests.get(url, cookies=COOKIES, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve LinkedIn profile for user ID {user_id}")

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting links and email addresses from the profile
    links = [a['href'] for a in soup.find_all('a', href=True) if 'linkedin.com' not in a['href']]
    emails = [a['href'][7:] for a in soup.find_all('a', href=True) if 'mailto:' in a['href']]

    return {'links': links, 'emails': emails}
