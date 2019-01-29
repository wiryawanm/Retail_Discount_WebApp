from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio 
import time
from xvfbwrapper import Xvfb
import requests
def search(item):
    master_arr = []
    # display = Xvfb()
    # display.start()
    searchTerm = item
    driver = webdriver.Firefox()
    driver.get('https://www.asos.com/search/?q={}'.format(searchTerm))
    p_element = driver.find_elements_by_class_name('_3x-5VWa')
    for group_element in p_element:
        if 'Current price' in group_element.get_attribute('aria-label'):
            aria_label = group_element.get_attribute('aria-label')
            name = aria_label.split(',')[0]
            discPrice = aria_label.split()[-4][0:-1]
            regPrice = aria_label.split()[-1]
            link = group_element.get_attribute('href')
            img = group_element.find_element_by_class_name('_1FN5N-P').find_element_by_tag_name('img').get_attribute('src')
            # disc_percent = (regPrice-discPrice)/regPrice
            arr = [name, link, img, regPrice, discPrice, 'asos']
            master_arr.append(arr)
            print("Name:\t\t", name)
            print("Link:\t\t", link)
            print("Image:\t\t", img)
            print("Regular Price:\t", regPrice)
            print("Discount Price:\t", discPrice)
            print()

    for i in range(1):
        try:
            driver.find_element_by_class_name('_2HG66Ah').click()
            p_element = driver.find_elements_by_class_name('_3x-5VWa')
            for group_element in p_element:
                if 'Current price' in group_element.get_attribute('aria-label'):
                    aria_label = group_element.get_attribute('aria-label')
                    name = aria_label.split(',')[0]
                    discPrice = aria_label.split()[-4][0:-1]
                    regPrice = aria_label.split()[-1]
                    link = group_element.get_attribute('href')
                    img = group_element.find_element_by_class_name('_1FN5N-P').find_element_by_tag_name('img').get_attribute('src')
                    # disc_percent = (regPrice-discPrice)/regPrice
                    arr = [name, link, img, regPrice, discPrice, 'asos']
                    master_arr.append(arr)            
                    print("Name:\t\t", name)
                    print("Link:\t\t", link)
                    print("Image:\t\t", img)
                    print("Regular Price:\t", regPrice)
                    print("Discount Price:\t", discPrice)
                    print()
        except:
            continue
    driver.quit()
    # display.stop()
    return master_arr