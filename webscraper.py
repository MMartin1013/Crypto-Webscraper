from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

"""with open('../../Documents/Code/Portfolio/index.html', 'r') as page:
    content = page.read()
    soup = BeautifulSoup(content, 'lxml')
    print(f'Page: {page}\n\n')
    print(f'Content: {content}')
    print(f'Soup: {soup}')
    print(f'SoupPrettify: {soup.prettify()}')
"""

#Gets html page
page = urlopen('https://coinmarketcap.com')
#Creates soup from page with lxml parsing
soup = BeautifulSoup(page, 'lxml')

#Obtains tending companies
categories = soup.find_all(class_='sc-16r8icm-0 sc-1uagfi2-0 bdEGog sc-1rmt1nr-1 eCWTbV')
for category in categories: 
    category_Name = category.find(class_='sc-1rmt1nr-0 sc-1rmt1nr-3 jCyFIz').div.get_text()
    companies = category.find_all(class_='sc-1rmt1nr-4')
    print(f'{category_Name}: ')
    for company in companies:
        #Obcures trending companies stats
        name = company.find(class_='sc-16r8icm-0').get_text()
        rank = company.find(class_='rank').get_text()
        price_Change = company.find(class_='price-change').get_text()

        print(f'Rank: {rank} Name: {name} Price Change: {price_Change}')
    print('\n')

