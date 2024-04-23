from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# IDファイルを読み込む
#with open('C:/Users/user/Desktop/Auto_login/ID.txt', 'r', encoding='UTF-8') as ID: #ノートパソコン用
with open('C:/Users/PC_User/OneDrive/デスクトップ/Auto_login/Auto_login/ID.txt', 'r', encoding='UTF-8') as ID: #デスクトップパソコン用
    IDdata = ID.read()

# PWファイルを読み込む
#with open('C:/Users/user/Desktop/Auto_login/PW.txt', 'r', encoding='UTF-8') as PW: #ノートパソコン用
with open('C:/Users/PC_User/OneDrive/デスクトップ/Auto_login/Auto_login/PW.txt', 'r', encoding='UTF-8') as PW: #デスクトップパソコン用
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
elem_login_btn = driver.find_element(By.XPATH, "//input[@value='ログイン']") # ログインボタンのXPath
elem_login_btn.click()

# ログイン後のページが読み込まれるのを待つ
wait = WebDriverWait(driver, 3)
elem_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title=取引]")))

# 新規注文ページへ遷移
elem_menu.click()
link = driver.find_element(By.LINK_TEXT, '国内株式')
link.click()

# ページが閉じるのを待つために適切な待機時間を設定する
time.sleep(3)

# ブラウザを閉じる
driver.quit()
