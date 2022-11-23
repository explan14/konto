import pandas as pd
import requests
from bs4 import BeautifulSoup
import crypto

crypto_name_list = []
crypto_price_list = []
crypto_market_cap_list = []
crypto_circuling_supply_list = []
crypto_symbol_list = []


df = pd.DataFrame()
#create a function to scrape the data
def scarpe(date= '20220612/'):
    #get the url of the website that we want to scrape
    url = 'https://coinmarketcap.com/historical/' +date
    #make a request to the website
    webpage = requests.get(url)
    #parse the text from the website
    soup = BeautifulSoup(webpage.text, 'html.parser')
    #get the table row element
    tr = soup.find_all('tr', attrs={'class':'cmc-table-row'})
    #create a count variable for the number of crypto currencies that we want to scrape
    count = 0 
    #loop throught every row to gather the data/ information
    for row in tr:
        #if the count is reached then break out of the loop
        if count == 11:
            break
        count = count + 1
        #store the name of the currency into a variable
        #find the td element(or column) to later get the currency name
        name_column = row.find('td', attrs={'class' : 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        crypto_name = name_column.find('a', attrs={'class': 'cmc-table__column-name--name cmc-link'}).text.strip()
        #store the currency of the currency cap into a variable
        crypto_market_cap = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
        #find and store the crypto price
        crypto_price = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
        #find and store crypto supply and symbol
        crypto_circuling_supply_and_symbol = row.find('td', attrs={'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
        #split the data 
        crypto_circuling_supply = crypto_circuling_supply_and_symbol.split(' ')[0]
        crypto_symbol = crypto_circuling_supply_and_symbol.split(' ')[1]


        #append the data to the lists
        crypto_name_list.append(crypto_name)
        crypto_market_cap_list.append(crypto_market_cap)
        crypto_price_list.append(crypto_price)
        crypto_circuling_supply_list.append(crypto_circuling_supply)
        crypto_symbol_list.append(crypto_symbol)


#run the scrape function
scarpe(date= '20220612/')

#store the data into a dataframe to help organize the data
df['Name'] = crypto_name_list
df['Market Cap'] = crypto_market_cap_list
df['Price'] = crypto_price_list
df['Circuling supply'] = crypto_circuling_supply_list
df['Symbol'] = crypto_symbol_list


print(df)
