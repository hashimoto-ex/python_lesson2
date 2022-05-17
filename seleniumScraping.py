import imp
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

chrome_path = r'C:\Users\YUTO\Desktop\python_lesson\chromedriver'
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

driver.quit()



