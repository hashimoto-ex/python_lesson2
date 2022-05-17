import imp
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

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


driver.quit()



