import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from undetected_chromedriver import C
from webdriver_manager.chrome import ChromeDriverManager
url = "https://play.google.com/store/apps/details?id=com.skyhealth.glucosebuddyfree"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.current_window_handle
about_app = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[2]/div/section/div/div[1]'))
)
print(about_app.text)

WebDriverWait(driver,220).until(EC.presence_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[4]/section/div/div/div[5]/div/div/button'))).click()

count = 0
SCROLL_PAUSE_TIME = 1

re = list()
while True:
    last_height = driver.execute_script("return document.querySelectorAll('.fysCi')[0].scrollHeight")
    driver.execute_script(f"document.querySelectorAll('.fysCi')[0].scrollTo(0, {last_height});")
    last_height = last_height + last_height
    time.sleep(SCROLL_PAUSE_TIME)
    reviews = driver.find_elements(By.CLASS_NAME,'h3YV2d')
    len(reviews) + len()
    if len(reviews) == 1000:
        break



df = pd.DataFrame(columns=["Reviews"])
for i in range(len(reviews)):
    df.loc[len(df.index)]=reviews[i].text
    print(f"index{i}",reviews[i].text)

df.to_csv("review.csv",index=False)
time.sleep(10)
