from selenium import webdriver
from time import sleep
from parsel import selector
import csv

google_query=''

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.google.com')
sleep(0.5)
qu = driver.find_element_by_name("q")
qu.send_keys(google_query)
sleep(0.5)
qu.send_keys(u'\ue007')
sleep(2)

data = driver.find_elements_by_class_name("LC20lb")
names = [txt.text for txt  in data]
sleep(0.2)
for i in range (1 , 30):
        s = driver.find_element_by_id("pnnext")
    s.click()
    sleep(0.2)
    data = driver.find_elements_by_class_name("LC20lb")
    names.extend([txt.text for txt  in data])
    sleep(0.2)


writer = csv.writer(open("data.csv", 'w'))

for name in names:
    writer.writerow(name.split("-"))

