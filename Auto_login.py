from selenium import webdriver#←seleniumからwebdriverをインポートします。変更不要です。

#↓IDファイル名や置き場を書き換えて下さい。
ID = open('C:/Users/user/Desktop/Auto_loginID.txt', 'r', encoding='UTF-8')
IDdata = ID.read()

#↓PWファイル名や置き場を書き換えて下さい。
PW = open('C:/Users/user/Desktop/Auto_loginPW.txt', 'r', encoding='UTF-8')
PWdata = PW.read()

#↓chromedriverの置き場を書き換えて下さい。
driver = webdriver.Chrome("C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\chromedriver.exe")
driver.get("https://www.sbisec.co.jp/ETGate")

#↓ログインIDの自動入力です。変更不要
elem_id_word = driver.find_element_by_name("user_id")#←現在のSBI証券の要素名
elem_id_word.send_keys(IDdata)

#↓ログインPWの自動入力です。変更不要
elem_pw_word = driver.find_element_by_name("user_password")#←現在のSBI証券の要素名
elem_pw_word.send_keys(PWdata)

#↓ログインボタンの自動入力です。変更不要
elem_login_btn = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/form/div/div/div/p[2]/a/input")#←現在のSBI証券のログインボタンのxpathです。
elem_login_btn.click()
