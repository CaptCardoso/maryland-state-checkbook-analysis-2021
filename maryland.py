import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import random



all_pages = []
for i in range(1,3):
    url = 'https://www.openthebooks.com/maryland-state-checkbook/?Year_C=2021&C_PG=' + str(i)
    
    

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.find('table', {'class':'employer-detail-table'})
    
    header = []
    for head in table.find_all('th'):
        header.append(head.text)

    for row in table.find_all('tr')[1:]:
        count = 0
        payout = {}
        for cell in row.find_all('td'):        
            payout[header[count]] = cell.text.strip()
            count += 1
        all_pages.append(payout)
    time.sleep(5)

df = pd.DataFrame(all_pages)

df.to_csv('Maryland_spending_2021.csv')