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
    driver.get('https://www.uniqlo.com/uk/en/search-results?q={}'.format(searchTerm))
    for i in range(8):
        try:
            driver.find_element_by_class_name('algolia-viewmore-link').click()
            time.sleep(1)
        except:
            continue
    p_element = driver.find_elements_by_class_name('disc-price')
    for discPrice in p_element:
        if(discPrice.text != ""):
            link = discPrice.find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_xpath('..')
            name = discPrice.find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_class_name('algolia-prods-item-title')
            img = discPrice.find_element_by_xpath('..').find_element_by_xpath('..').find_element_by_class_name('algolia-prods-item-img-container').find_element_by_class_name('algolia-prods-item-img-original')
            regPrice = discPrice.find_element_by_xpath('..').find_element_by_class_name('reg-price')
            arr = [name.text, link.get_attribute('href'), img.get_attribute('src'),
                    regPrice.text, discPrice.text, 'uniqlo']
            master_arr.append(arr)
            print("Name:\t\t", name.text)
            print("Link:\t\t", link.get_attribute('href'))
            print("Image:\t\t", img.get_attribute('src'))
            print("Regular Price:\t", regPrice.text)
            print("Discount Price:\t", discPrice.text)
    driver.quit()
    # display.stop()
    return master_arr