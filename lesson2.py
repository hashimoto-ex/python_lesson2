import imp
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import pandas as pd


chrome_path = ''
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)

url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = 'プログラミング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput') #要素検証で探したキーワード検索ボックスのクラス名をつかう
search_box.send_keys(query) #キーワードを入れる
search_box.submit() #ボタン押す

sleep(3)

height = 1000
while height < 3000:
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height += 100
    
    sleep(1)
d_list = []

#画像の要素を取得する
elements = driver.find_elements_by_class_name('sw-Thumbnail')
for i, element in enumerate(elements, start=1):
    name = f'{query}_{i}'
    raw_url = element.find_element_by_class_name('sw-ThumbnailGrid__details') #画像のURL
    yahoo_image_url = element.find_element_by_tag_name('img').get_attribute('src')
    title = element.find_element_by_tag_name('img').get_attribute('alt')
    d = {
        'filename': name,
        'raw_url': raw_url,
        'yahoo_image_url': yahoo_image_url,
        'title': title
    }
    d_list.append(d)

df = pd.DataFrame(d_list)
df.to_csv('image_urls_20220517.csv')
driver.quit()



