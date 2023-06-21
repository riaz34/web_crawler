from selenium import webdriver
import time
#select the driver path
driver = webdriver.Chrome("/home/lighty/Downloads/Compressed/chromedriver_linux64_1/chromedriver")
driver.maximize_window()
#select the website
driver.get("https://google.com/")

links = []

elements = driver.find_elements_by_tag_name("a")
for element in elements:
    link = element.get_attribute("href")
    if link:
        links.append(link)

for link in links:
    time.sleep(5)          # click a link after 5 sec
    driver.get(link)

driver.quit()