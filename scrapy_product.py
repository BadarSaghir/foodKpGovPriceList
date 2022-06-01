import requests
from bs4 import BeautifulSoup


def getRelevantData():
    
    filter_data= {
        'labels':[],
        'data':[]
    }
    res = requests.get('https://food.kp.gov.pk/page/price_list')
    bs4=BeautifulSoup((res.text), 'html.parser')
    tbody:BeautifulSoup= bs4.find('tbody')
    tr:[BeautifulSoup]=tbody.find_all('tr')
    lb=tr[0].text.split()
    filter_data['labels'].append(lb)
    print(filter_data)
    for i in range(1,len(tr)):
        td=tr[i].find_all('td')
        lb=[ td[t].text.strip()  for t in range(len(td))  ]
        filter_data['data'].append(lb)
    
    return filter_data

try:
    fil=getRelevantData()
    print(fil)
except:
    print("String is here")