from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://es.wikipedia.org/wiki/Granada_Club_de_F%C3%BAtbol")
tabla = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[16]')
print(tabla.text)