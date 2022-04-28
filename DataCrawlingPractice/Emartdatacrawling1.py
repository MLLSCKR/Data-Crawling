# 전체 page에 있는 모든 데이터 Crawling 연습(image 파일 제외하고 상품명과 상품가격만 가져오는 경우)

# next page 선택 xpath
# 2nd page //*[@id="area_itemlist"]/div[2]/a[1]
# 3rd page //*[@id="area_itemlist"]/div[2]/a[2]
# 10th page //*[@id="area_itemlist"]/div[2]/strong

# web page crawling시 새로운 web page가 open 될때까지 대기하기 위해서 selenium 내의 함수 implicitly_wait를 사용한다.
# driver.implicitly_wait(10) -> 다음 웹페이지가 열릴때 까지 최대 10초까지는 기다려주겠다는 의미이다.
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('chromedriver')
driver.get('http://emart.ssg.com/')
driver.find_element_by_xpath('//*[@id="e_gnb"]/div/div[1]/div[2]/ul[1]/li[9]/a').click()

pdname_list = []
pdprice_list = []

pattern1 = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pattern2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
check_fin = True

driver.implicitly_wait(10)

for j in pattern1:
    for i in range(1, 81):
        try:
            product_name = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li[' + str(i) + ']/div[2]/div[2]/div/a/em[1]').text
            product_price = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li[' + str(i) + ']/div[2]/div[3]/div[1]/em').text
            pdname_list.append(product_name)
            pdprice_list.append(product_price)

        except Exception as e:
            print(e)

        finally:
            pass


    try:
        driver.find_element_by_xpath('//*[@id="area_itemlist"]/div[2]/a[' + str(j) + ']').click()
            
    except Exception as e:
        print(e)
                
    finally:
        pass

while True:
    for j in pattern2:
        for i in range(1, 81):
            try:
                product_name = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li[' + str(i) + ']/div[2]/div[2]/div/a/em[1]').text
                product_price = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li[' + str(i) + ']/div[2]/div[3]/div[1]/em').text
                pdname_list.append(product_name)
                pdprice_list.append(product_price)

            except Exception as e:
                print(e)
                break

            finally:
                pass


        try:
            driver.find_element_by_xpath('//*[@id="area_itemlist"]/div[2]/a[' + str(j) + ']').click()
            
        except Exception as e:
            print(e)
            check_fin = False
            break
                
        finally:
            pass
    
    if check_fin == False:
        break

df1 = pd.DataFrame({'상품명' : pdname_list, '가격' : pdprice_list})

driver.quit()