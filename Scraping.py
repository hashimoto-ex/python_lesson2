import requests
import sys
from bs4 import BeautifulSoup
from pathlib import Path #フォルダ操作モジュール
import urllib #url操作モジュール
import time #時間操作モジュール

res = requests.get('https://joytas.net/kaba/') #get通信
#res = requests.post('https://joytas.net/php/calc.php',data={'x':10,'y':7})

res.encoding = res.apparent_encoding #文字化け対策

soup = BeautifulSoup(res.text,'html.parser')

#Pathオブジェクト作成
out_folder = Path('downloaded')
out_folder.mkdir(exist_ok=True)
#print(soup)

#print(sys.executable)
# ele = soup.find('td') #要素を取得 1つだけ
# print(ele.text)

#別の取得方法
#div = soup.find(id = 'headerImageBox')
# div = soup.find(id = 'td')

imgs = soup.select('img')
for img in imgs:
    src = img.get('src')
    img_url=urllib.parse.urljoin(load_url,src)

    #get通信で画像をロード
    loaded_img=requests.get(img_url)

    #ファイル名取得
    file_name=img.get('src').split('/')[-1]

    #保存画像パス
    out_path=out_folder.joinpath(file_name)

    #wbはバイナリ書き込み
    with open(out_path,"wb") as file:
        #contentはバイナリデータ
        file.write(loaded_img.content)

    #DOS攻撃にならないように時間(1秒)あける
    time.sleep(1)

#演習
imgs = soup.find_all('td') #要素複数取得
# newImgs = []
# for i in range(imgs):
#     if i % 3 == 0:
#         newImgs.append(imgs[i])
#         # print(imgs[i].text)
#     else:
#         continue
i = 0

for img in imgs:
    if (i % 3) == 0:
        print(img.text) #属性にはget
        i += 1
    else:
        i += 1
        continue

links = soup.select('li a')

#ファイル書き込み
with open('zoo.txt','w',encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')
    

    



