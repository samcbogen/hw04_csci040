import requests
from bs4 import BeautifulSoup

keyword='autograph'
page_number='1'
results = []


for i in range(1,11):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i))
    print('r.status_code',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')



    '''
    items = soup.select('.s-item__title')
    for item in items:
        print('item=',item.text)
    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    ''' 
    boxes = soup.select('li.s-item--watch-at-corner.s-item')

    
    for box in boxes:
        result = {}
        names = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for name in names:
            result['name'] = name.text # using title because that's what we're calling it in the assignment
        prices = box.select('.s-item__price') # extracting price css selector inside of box, if keep at soup.select it will browse the entire website still 
        for price in prices: #
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
            result['status'] = status.text
        results.append(result)
    print('len(results)=',len(results))

import json 
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
