from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio 
import time    
from xvfbwrapper import Xvfb
import requests
def search(item):
    master_arr = []
    searchTerm = item
    # display = Xvfb()
    # display.start()
    driver = webdriver.Firefox()
    
    driver.get('https://www2.hm.com/en_gb/search-results.html?q={}'.format(searchTerm))
    # time.sleep(5)
    # driver.find_element_by_class_name('modalconfirm').click()
    # for i in range(8):
    #     try:
    #         driver.find_element_by_class_name('js-load-more').click()
    #         time.sleep(2)
    #     except:
    #         continue
    p_element = driver.find_elements_by_class_name('sale')
    for discPrice in p_element:
        main_element = discPrice.find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_class_name('image-container').find_element_by_class_name('item-link')
        link = main_element.get_attribute('href')
        name = main_element.get_attribute('title')
        img = main_element.find_element_by_class_name('item-image')
        regPrice = discPrice.find_element_by_xpath('..').find_element_by_class_name('regular')
        arr = [name, link, img.get_attribute('src'), regPrice.text, discPrice.text, 'h&m']
        master_arr.append(arr)
        print("Name:\t\t", name)
        print("Link:\t\t", link)
        print("Image:\t\t", img.get_attribute('src'))
        print("Regular Price:\t", regPrice.text)
        print("Discount Price:\t", discPrice.text)
        print()
    driver.quit()
    # display.stop()
    return master_arr