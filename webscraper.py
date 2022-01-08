from urllib.request import urlopen
from bs4 import BeautifulSoup
#This program gathers and stores information from the coin market cap website to be displayed in the gui


#Class to hold company information
class Company:
    def __init__(self):
        self.name = None
        self.rank = None
        self.pricechange = None
        self.dayprice = None
        self.sevendayprice = None
        self.marketcap = None
        self.volume = None
        self.circulatingsupply = None
        self.img = None

    def get_name(self):
        return 'Name: ' + self.name

    def get_rank(self):
        return 'Rank: ' + self.rank
    
    def get_pricechange(self):
        return 'Price: ' + self.pricechange

    def get_dayprice(self):
        return '24H%: ' + self.dayprice if self.dayprice != None else ''
    
    def get_sevendayprice(self):
        return '7D%: ' + self.sevendayprice if self.sevendayprice != None else ''
    
    def get_marketcap(self):
        return 'Market Cap: ' + self.marketcap if self.marketcap != None else ''

    def get_volume(self):
        return 'Volume: ' + self.volume if self.volume != None else ''

    def get_circulatingsupply(self):
        return 'Circulating Supply: ' + self.circulatingsupply if self.circulatingsupply != None else ''   
        
    def get_img(self):
        return 'Img: ' + self.img if self.img != None else ''

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.get_name(),self.get_rank(),self.get_pricechange(),self.get_dayprice(),self.get_sevendayprice(),self.get_marketcap(),self.get_volume(),self.get_circulatingsupply(),self.get_img()).strip()

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.get_name(),self.get_rank(),self.get_pricechange(),self.get_dayprice(),self.get_sevendayprice(),self.get_marketcap(),self.get_volume(),self.get_circulatingsupply(),self.get_img()).strip()

#Class to hold category information
class Category:
    
    def __init__(self):
        self.name = None;
        self.companies = []
    
    def get_name(self):
        return self.name + '\n'

    def get_companies(self):
        return self.companies    

    def __repr__(self):
        s = '{}\n'.format(self.get_name())
        for company in self.companies:
            s += '{}\n'.format(company)

        return s


class WebScraper:

    #Gets html page
    #Creates soup from page with lxml parsing
    def __init__(self):
        self.page = urlopen('https://coinmarketcap.com')
        self.soup = BeautifulSoup(self.page, 'lxml')

    #Returns an
    def get_categories(self):  
        self.page = urlopen('https://coinmarketcap.com')
        self.soup = BeautifulSoup(self.page, 'lxml')
        #Return value
        info = []
        #Obtains tending companies
        categories = self.soup.find_all(class_='sc-16r8icm-0 sc-1uagfi2-0 bdEGog sc-1rmt1nr-1 eCWTbV')
        for category in categories: 
            #New object to hold category information
            newCategory = Category()
            
            #Obtains name of category and array of companies for that category
            newCategory.name = category.find(class_='sc-1rmt1nr-0 sc-1rmt1nr-3 jCyFIz').div.get_text()
            companies = category.find_all(class_='sc-1rmt1nr-4')
            
            #Gets information for each company in the category
            for company in companies:
                #New object to hold company information
                newCompany = Company()
                
                #Obcures trending companies name and rank and stores them in newcomapny class
                newCompany.name = company.find(class_='sc-16r8icm-0').get_text()
                newCompany.rank = company.find(class_='rank').get_text()
            
                #Polarity used to calculate whether the price is up or down
                polarity = company.find(class_='icon-Caret-up')
                #Stores price change based on polarity if the company hasn't been recently added
                
                #Stores neutral price otherwise
                if(newCategory.name != 'Recently Added'):
                    newCompany.pricechange = '-' + company.find(class_='price-change').get_text() if (polarity == None) else  '+' + company.find(class_='price-change').get_text()
                else:
                    newCompany.pricechange = company.find(class_='price-change').get_text()

                #Adds new company to the list of companies in new Category
                newCategory.companies.append(newCompany)
                
            #Adds new category to the table
            info.append(newCategory)
        return info

#Table of cryptocurrencies

    #Gets info from the first 10 elements on the coin market cap table
    def get_table(self):
        self.page = urlopen('https://coinmarketcap.com')
        self.soup = BeautifulSoup(self.page, 'lxml')
        #Return value
        info = []
        #Obtains table and its rows
        table = self.soup.find(class_='h7vnx2-2 czTsgW cmc-table').find('tbody')
        rows = table.find_all('tr')

        #Gets the first 5 items
        for i in range(5):
            #New instance of company class to store company information
            newCompany = Company()
            
            #Obtains their statistics and stores them into new company object
            newCompany.rank = rows[i].find(class_='sc-1eb5slv-0 etpvrL').get_text()
            newCompany.name = rows[i].find(class_='sc-16r8icm-0 sc-1teo54s-1 dNOTPP').find('p').get_text()
            newCompany.pricechange = rows[i].find(class_='sc-131di3y-0 cLgOOr').get_text()
            prices = rows[i].find_all(class_='sc-15yy2pl-0')
            dayprice = prices[0]
            sevendayprice = prices[1]
            newCompany.marketcap = rows[i].find(class_='sc-1ow4cwt-1 ieFnWP').get_text()
            newCompany.volume = rows[i].find(class_='sc-1eb5slv-0 hykWbK font_weight_500').get_text()
            newCompany.circulatingsupply = rows[i].find(class_= 'sc-1eb5slv-0 kZlTnE').get_text()
            newCompany.image = rows[i].find('img').get('src')

            #24H prices and 7d Prices have a chance to not exist
            if(dayprice != None):
                polarity = dayprice.find(class_='icon-Caret-up')
                newCompany.dayprice = '-' + dayprice.get_text() if (polarity == None) else  '+' + dayprice.get_text()
            
            if(sevendayprice != None):
                polarity = sevendayprice.find(class_='icon-Caret-up')
                newCompany.sevendayprice = '-' + sevendayprice.get_text() if (polarity == None) else  '+' + sevendayprice.get_text()

            #Adds new company to list
            info.append(newCompany)

        return info

    
if __name__ == '__main__':
    scraper = WebScraper()
    print(scraper.get_categories())
    print(scraper.get_table())