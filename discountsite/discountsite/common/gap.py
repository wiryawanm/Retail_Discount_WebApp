from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio 
import time    
import requests
from xvfbwrapper import Xvfb
def search(item):
    master_arr = []
    searchTerm = item
    # display = Xvfb()
    # display.start()
    driver = webdriver.Firefox()
    driver.get('https://www.gap.co.uk/search?q={}'.format(searchTerm))
    p_element = driver.find_elements_by_class_name('product-sales-price')
    for discPriceElement in p_element:
        discPrice = discPriceElement.find_element_by_tag_name('a').text
        regPrice = discPriceElement.find_element_by_xpath('..').find_element_by_class_name('product-standard-price').find_element_by_tag_name('a').text
        main_element = discPriceElement.find_element_by_xpath('..').find_element_by_xpath('..')
        name = main_element.find_element_by_class_name('product-name').find_element_by_tag_name('a').text
        img = main_element.find_element_by_class_name('product-image').find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('src')
        link = main_element.find_element_by_class_name('product-image').find_element_by_tag_name('a').get_attribute('href')
        # disc_percent = (regPrice-discPrice)/regPrice
        arr = [name, link, img, regPrice, discPrice, 'gap']
        master_arr.append(arr)        
        print("Name:\t\t", name)
        print("Link:\t\t", link)
        print("Image:\t\t", img)
        print("Regular Price:\t", regPrice)
        print("Discount Price:\t", discPrice)

        print()
    driver.quit()
    # display.stop()
    return master_arr

