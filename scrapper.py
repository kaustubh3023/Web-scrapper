import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://www.flipkart.com/motorola-edge-50-coming-soon-store?param=27993&otracker=clp_bannerads_1_21.bannerAdCard.BANNERADS_A_mobile-phones-store_JKBSEDG6KDZN'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and print the title of the page
    title = soup.find('title').text
    print('Page title:', title)

    # Example: Find and print all paragraph texts
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.text)
else:
    print('Failed to retrieve the page')