from selenium import webdriver
from selenium.webdriver.common.by import By
import time

txt_f = open("./bookchart.txt","w")
chromedriver = r'./chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(10)

driver.get("https://www.coupang.com/np/categories/115673")

lis = driver.find_element(By.ID, 'productList').find_elements(By.TAG_NAME, 'li')

for li in lis:
    try:
        print('Product: ' + li.find_element(By.CLASS_NAME, 'name').text)
        print('Price: ' + li.find_element(By.CLASS_NAME, 'price-value').text)
        print('Delivery: ' + li.find_element(By.CLASS_NAME, 'delivery').text)
        print('URL: ' + li.find_element(By.CLASS_NAME, 'baby-product-link').get_attribute('href'))
        print('-'*100)

    except Exception:
        pass

driver.quit()





