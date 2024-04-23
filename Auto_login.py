from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# IDファイルを読み込む
#with open('C:/Users/user/Desktop/Auto_login/ID.txt', 'r', encoding='UTF-8') as ID: #ノートパソコン用
with open('C:/Users/PC_User/OneDrive/デスクトップ/Auto_login/Auto_login/ID.txt', 'r', encoding='UTF-8') as ID:
    IDdata = ID.read()

# PWファイルを読み込む
#with open('C:/Users/user/Desktop/Auto_login/PW.txt', 'r', encoding='UTF-8') as PW: #ノートパソコン用
with open('C:/Users/PC_User/OneDrive/デスクトップ/Auto_login/Auto_login/PW.txt', 'r', encoding='UTF-8') as PW:
    PWdata = PW.read()

# Chrome WebDriverを初期化
driver = webdriver.Chrome()

# 指定したURLにアクセス
driver.get("https://www.sbisec.co.jp/ETGate")

# ログインIDの自動入力
elem_id_word = driver.find_element(By.NAME, "user_id")
elem_id_word.send_keys(IDdata)

# ログインPWの自動入力
elem_pw_word = driver.find_element(By.NAME, "user_password")
elem_pw_word.send_keys(PWdata)

# ログインボタンの自動入力
elem_login_btn = driver.find_element(By.XPATH, "//input[@value='ログイン']")
elem_login_btn.click()

# ログイン後のページが読み込まれるのを待つ
wait = WebDriverWait(driver, 3)
elem_menu = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[title=取引]")))

# 新規注文ページへ遷移
elem_menu.click()
link = driver.find_element(By.LINK_TEXT, '国内株式')
link.click()

# 取引方法の選択
trade_type_dict = {
    "現物買": "genK",
    "現物売": "genU",
    "信用新規買": "shinK",
    "信用新規売": "shinU"
}

trade_type = "現物買"
selected_trade = trade_type_dict.get(trade_type)
if selected_trade:
    driver.find_element(By.ID, selected_trade).click()
else:
    print("指定された取引方法が見つかりませんでした。")

# 現物買、現物売、信用新規買、信用新規売の選択
trade_type_key = "現物買"
if trade_type_key in trade_type_dict:
    driver.find_element(By.ID, trade_type_dict[trade_type_key]).click()
else:
    print("指定された取引方法が見つかりませんでした。")

# 証券コードの入力
driver.find_element(By.NAME, "stock_sec_code").send_keys("4755")

# 株数の入力
driver.find_element(By.NAME, "input_quantity").send_keys("100")

# 価格の条件入力
in_sasinari_kbn = " "

# 指定されたin_sasinari_kbnに対応するラジオボタンを選択
if in_sasinari_kbn in ["N", "G", " "]:
    driver.find_element(By.CSS_SELECTOR, 'input[name="in_sasinari_kbn"]').click()
    time.sleep(1)  # ポップアップが表示されるまで待機
    # ポップアップで選択
    if in_sasinari_kbn == "N":
        driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)  # 成行を選択
    elif in_sasinari_kbn == "G":
        driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN * 2)  # 逆指値を選択
    driver.switch_to.active_element.send_keys(Keys.ENTER)  # Enterで確定
else:
    print("指定された価格情報が見つかりませんでした。")

# 指値が選択された場合の処理
if in_sasinari_kbn == " ":
    # 指値が選択された場合、条件なしのオプションを選択
    sasine_condition_select = driver.find_element(By.NAME, "sasine_condition")
    sasine_condition_select.click()
    driver.find_element(By.CSS_SELECTOR, 'select[name="sasine_condition"] option[value=" "]').click()
    driver.find_element(By.NAME, "input_price").send_keys("100") #価格を入力する項目


# ページが閉じるのを待つために適切な待機時間を設定する
time.sleep(3)

# ブラウザを閉じる
driver.quit()
