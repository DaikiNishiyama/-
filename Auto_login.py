from selenium import webdriver
from selenium.webdriver.common.by import By

# IDファイルを読み込む
ID = open('C:/Users/user/Desktop/Auto_login/ID.txt', 'r', encoding='UTF-8')
IDdata = ID.read()

# PWファイルを読み込む
PW = open('C:/Users/user/Desktop/Auto_login/PW.txt', 'r', encoding='UTF-8')
PWdata = PW.read()

# Chrome WebDriverを初期化
driver = webdriver.Chrome()

# 指定したURLにアクセス
driver.get("https://www.sbisec.co.jp/ETGate")

# ログインIDの自動入力
elem_id_word = driver.find_element(By.NAME, "user_id") # 現在のSBI証券の要素名
elem_id_word.send_keys(IDdata)

# ログインPWの自動入力
elem_pw_word = driver.find_element(By.NAME, "user_password") # 現在のSBI証券の要素名
elem_pw_word.send_keys(PWdata)

# ログインボタンの自動入力
elem_login_btn = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td[2]/form/div/div/div/p[2]/a/input") # 現在のSBI証券のログインボタンのxpath
elem_login_btn.click()
