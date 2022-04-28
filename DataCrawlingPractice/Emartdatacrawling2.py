# 전체 page에 있는 모든 데이터 Crawling 연습(제품의 image 파일을 포함하여 Crawling 하는 경우)


from selenium import webdriver
import pandas as pd
import urllib.request

driver = webdriver.Chrome('chromedriver')
driver.get('http://emart.ssg.com/')
driver.find_element_by_xpath('//*[@id="e_gnb"]/div/div[1]/div[2]/ul[1]/li[9]/a').click()

pdname_list = []
pdprice_list = []
pdimage_list = []

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
            
            # 이미지 data url Crawling
            try:
                tempimg = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li['+ str(i) +']/div[1]/div[2]/a/img[1]')
                img_url = tempimg.get_attribute('src')
                pdimage_list.append(img_url)
            except Exception as e:
                print('예외가 발생했습니다.', e)
                pdimage_list.append('19세 이상 사용자 접근 가능 이미지')
            finally:
                pass
            
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
                
                # 이미지 data url Crawling
                try:
                    tempimg = driver.find_element_by_xpath('//*[@id="ty_thmb_view"]/ul/li['+ str(i) +']/div[1]/div[2]/a/img[1]')
                    img_url = tempimg.get_attribute('src')
                    pdimage_list.append(img_url)
                except Exception as e:
                    print('예외가 발생했습니다.', e)
                    pdimage_list.append('19세 이상 사용자 접근 가능 이미지')
                finally:
                    pass

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