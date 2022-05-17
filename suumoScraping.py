from bs4 import BeautifulSoup #importする順番はアルファベット順にするとなおよい
from time import sleep
import requests
import pandas as pd
from pprint import pprint

url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'

d_list = []
for i in range(1,4):
    print(f'd_listの長さ{len(d_list)}')
    target_url = url.format(i)
    #print(target_url)
    r = requests.get(target_url)
    sleep(1)
    soup = BeautifulSoup(r.text,'html.parser')

    
    contents = soup.find_all('div',class_='cassetteitem')
    for content in contents:
        #物件・建物情報を変数に格納
        detail = content.find('div',class_='cassetteitem-detail')
        #print(detail)
        #各部屋の情報を変数に格納
        table = content.find('table',class_='cassetteitem_other')
        title = detail.find('div',class_='cassetteitem_content-title').text

        address = detail.find('li',class_='cassetteitem_detail-col1').text
        access = detail.find('li',class_='cassetteitem_detail-col2').text
        age = detail.find('li',class_='cassetteitem_detail-col3').text

        #print(title,address,access,age)

        tr_tags = table.find_all('tr',class_='js-cassette_link')

        for tr_tag in tr_tags:
            floor,plice,first_fee,capacity = tr_tag.find_all('td')[2:6] #3番目から6番目を取得

            #print(floor,plice,first_fee,capacity)
            fee,management_fee = plice.find_all('li')
            deposit,gratuity = first_fee.find_all('li')
            madori,menseki = capacity.find_all('li')

            d = {
                'title':title,
                'address':address,
                'access':access,
                'age':age,
                'floor':floor,
                'fee':fee.text,
                'management_fee':management_fee.text,
                'deposit':deposit.text,
                'gratuity':gratuity.text,
                'madori':madori.text,
                'menseki':menseki.text
            }

        d_list.append(d)
# print('d_list[0]中身', sep='')
# pprint(d_list[0])
# print('d_list[1]中身', sep='')
# pprint(d_list[-1])
df = pd.DataFrame(d_list)

#print(df.head())

#print(len(df.title.unique()))
df.to_csv('test.csv',index=None, encoding='utf-8-sig')#文字コードを指定して文字化け対策する



