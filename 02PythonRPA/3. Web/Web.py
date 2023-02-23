from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

browser.get("http://daum.net")

browser.find_element_by_link_text