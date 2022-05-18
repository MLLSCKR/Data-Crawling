from selenium import webdriver

import pyautogui
import pandas as pd
# from multiprocessing import Pool
from time import sleep

driver = webdriver.Chrome('chromedriver')
driver.get('https://kr.investing.com/etfs/powershares-qqqq')

# 마우스 움직임
display_size = pyautogui.size()

for i in range (1, display_size.width, 400):
    for j in range(1, display_size.height, 400):
        pyautogui.moveTo(i, j)

sleep(3)
driver.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()

driver.find_element_by_xpath('//*[@id="pairSublinksLevel2"]/li[3]/a').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="widgetFieldDateRange"]').click()
driver.find_element_by_xpath('//*[@id="startDate"]').click()
sleep(0.5)
input_text = driver.find_element_by_id('startDate')
input_text.clear()
sleep(0.5)
input_text.send_keys('2000/01/01')
sleep(0.5)
driver.find_element_by_xpath('//*[@id="applyBtn"]').click()

sleep(3)

a = []
df = pd.DataFrame({'날짜': [], 'close': [], 'open': [], 'high': [], 'low': [], 'volume': [], 'fluctuations': []})

j = 0
check_fin = True

print("Start Check Data")

while True:
    a = []
    k = j+1
    for i in range(1, 8):
        try:
            a.append(driver.find_element_by_xpath('//*[@id="curr_table"]/tbody/tr[' + str(k) + ']/td[' + str(i) + ']').text)

        except Exception as e:
            print(e)
            check_fin = False
            break

        finally:
            pass
    
    if check_fin == False:
        break
    
    j = j+1
    
    print(a)
    
    df.loc[j] = a

driver.quit()