from urllib.request import urlopen
from bs4 import BeautifulSoup

#Gets html page
page = urlopen('https://coinmarketcap.com')
#Creates soup from page with lxml parsing
soup = BeautifulSoup(page, 'lxml')

#Obtains tending companies
categories = soup.find_all(class_='sc-16r8icm-0 sc-1uagfi2-0 bdEGog sc-1rmt1nr-1 eCWTbV')
for category in categories: 
    #Obtains name of category and array of companies for that category
    category_Name = category.find(class_='sc-1rmt1nr-0 sc-1rmt1nr-3 jCyFIz').div.get_text()
    companies = category.find_all(class_='sc-1rmt1nr-4')
    
    print(f'{category_Name}: ')
    for company in companies:
        #Obcures trending companies name and rank
        name = company.find(class_='sc-16r8icm-0').get_text()
        rank = company.find(class_='rank').get_text()
       
        #Polarity used to calculate whether the price is up or down
        polarity = company.find(class_='icon-Caret-up')
        #Stores price change based on polarity if the company hasn't been recently added
        #Stores neutral price otherwise
        if(category_Name != 'Recently Added'):
            price_Change = '-' + company.find(class_='price-change').get_text() if (polarity == None) else  '+' + company.find(class_='price-change').get_text()
        else:
            price_Change = company.find(class_='price-change').get_text()

        print(f'Rank: {rank} Name: {name} Price Change: {price_Change}')
    print('\n')

#Table of cryptocurrencies

#Obtains table and its rows
table = soup.find(class_='h7vnx2-2 czTsgW cmc-table').find('tbody')
rows = table.find_all('tr')

#Gets the first 10 items
for i in range(10):
    #Obtains their statistics
    rank = rows[i].find(class_='sc-1eb5slv-0 etpvrL').get_text()
    name = rows[i].find(class_='sc-16r8icm-0 sc-1teo54s-1 dNOTPP').find('p').get_text()
    price = rows[i].find(class_='sc-131di3y-0 cLgOOr').get_text()
    prices = rows[i].find_all(class_='sc-15yy2pl-0')
    twentyFourHourPrice = prices[0]
    sevenDayPrice = prices[1]
    marketCap = rows[i].find(class_='sc-1ow4cwt-1 ieFnWP').get_text()
    volume = rows[i].find(class_='sc-1eb5slv-0 hykWbK font_weight_500').get_text()
    circulatingSupply = rows[i].find(class_= 'sc-1eb5slv-0 kZlTnE').get_text()
    image = rows[i].find('img').get('src')

    #24H prices and 7d Prices have a chance to not exist
    if(twentyFourHourPrice != None):
        polarity = twentyFourHourPrice.find(class_='icon-Caret-up')
        twentyFourHourPrice = '-' + twentyFourHourPrice.get_text() if (polarity == None) else  '+' + twentyFourHourPrice.get_text()
    
    if(sevenDayPrice != None):
        polarity = sevenDayPrice.find(class_='icon-Caret-up')
        sevenDayPrice = '-' + sevenDayPrice.get_text() if (polarity == None) else  '+' + sevenDayPrice.get_text()



    print(f'Rank: {rank} Name: {name} Price: {price} 24Hr%: {twentyFourHourPrice} 7d%: {sevenDayPrice} MarketCap: {marketCap} Volume: {volume} CirculatingSupply: {circulatingSupply} Image: {image}')
