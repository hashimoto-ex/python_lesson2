import requests
import sys
from bs4 import BeautifulSoup
from pathlib import Path #フォルダ操作モジュール
import urllib #url操作モジュール
import time #時間操作モジュール


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
load_url='' #サイトのURL
res = requests.get(load_url,headers= headers) #get通信

res.encoding = res.apparent_encoding #文字化け対策

soup = BeautifulSoup(res.text,'html.parser')

out_folder = Path('downloaded')
out_folder.mkdir(exist_ok=True)


def numShaping(num) -> str: 
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

for i in range(1,100): 
    
    numStr = numShaping(i)
    targetRange = soup.find("img",alt=f'_0{numStr}') #alt 可変予定
    #print(f'対象範囲 :{targetRange}')
    print(f'{i}番目[{targetRange}]')
    if targetRange is None:
        print('保存が完了しました')
        break
    else:
        src = targetRange.get('src')
    #print(f'src:{src}')

    img_url=urllib.parse.urljoin(load_url,src)
    #print(f'img_url :{img_url}')
    loaded_img=requests.get(img_url) #get通信で画像をロード
    file_name=targetRange.get('src').split('/')[-1] #ファイル名取得
    #print(f'file_name :{file_name}')
    out_path=out_folder.joinpath(file_name) #保存画像パス
    print(f'out_path :{out_path}')

    header = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0" } # 追加
    request = urllib.request.Request(img_url, headers=header)

    with urllib.request.urlopen(request) as web_file:
        data = web_file.read()
        with open(out_path,"wb") as file: #wbはバイナリ書き込み
            print(f'{file_name}:保存成功')
            file.write(data)
        time.sleep(1)

    



