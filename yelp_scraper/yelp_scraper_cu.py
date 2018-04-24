import json
from selenium import webdriver as wd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re

def CU_REST():
    url = "https://www.yelp.com/search?find_loc=Urbana+Champaign,+IL"
    # Linux
    # driver = wd.Chrome('/usr/bin/chromedriver')
    # Windows
    driver = wd.Chrome('C:/Yoo/git/cs411/yelp_scraper/chromedriver.exe')
    # Mac
    # driver = wd.Chrome()
    driver.get(url)
    jsonlist = []

    for j in range(40):
        nitems = len(driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]').find_elements_by_xpath('li[@class="regular-search-result"]'))
        for i in range(nitems):
            dic = {}

            while (1):
                try:
                    pagelist = driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]')
                    result = pagelist.find_elements_by_xpath('li[@class="regular-search-result"]')[i]
                    imageurl = result.find_element_by_tag_name("img").get_attribute("src")
                    dic['imageurl'] = imageurl
                    item = result.find_element_by_class_name("js-analytics-click")
                    # item.click()

                    break
                except WebDriverException:
                    print('err')
                    pass
            driver.implicitly_wait(10)
            main_window = driver.current_window_handle
            item.send_keys(Keys.CONTROL + Keys.RETURN)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            dic["title"] = driver.find_element_by_class_name("biz-page-title").text
            dic["category"] = "Restaurants"
            dic["addr"] = driver.find_element_by_class_name("street-address").text.replace('\n',' ')
            dic["city"] = "Urbana Champaign, IL"
            try:
                rating = driver.find_element_by_class_name("rating-very-large").get_attribute("title")
                dic["rating"] = re.search(r'\d.\d', rating).group(0).strip()
            except NoSuchElementException:
                dic["rating"] = "N/A"
            try:
                table = driver.find_element_by_class_name("hours-table")
                for i in range(1, 8):
                    hours = table.find_element_by_xpath("tbody/tr["+str(i)+"]/td[1]").text
                    if len(hours.strip()) > 8:
                        break

            except NoSuchElementException:
                hours = "N/A - N/A"

            dic["hours"] = hours

            geo = json.loads(driver.find_element_by_class_name("lightbox-map").get_attribute("data-map-state"))
            try:
                lat = geo['center']['latitude']
                lon = geo['center']['longitude']

            except e:
                lat = 'N/A'
                lon = 'N/A'

            dic["lat"] = lat
            dic["lon"] = lon
            print(dic)
            jsonlist.append(dic)
            # driver.back()
            # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            driver.close()
            driver.switch_to_window(main_window)

        driver.implicitly_wait(10)
        next = driver.find_element_by_xpath("//a[@class='u-decoration-none next pagination-links_anchor']")

        while(1):
            try:
                next.click()
                break
            except WebDriverException:
                print("err", j)
                pass

        driver.implicitly_wait(10)

    with open('yelp_cu_rest.json', 'w') as fp:
        json.dump(jsonlist, fp)


    driver.close()
    print("CU REST DONE")

def CU_PLACE():
    url = "https://www.yelp.com/search?find_desc=things+to+do&find_loc=Urbana+Champaign,+IL"
    #linux
    # driver = wd.Chrome('/usr/bin/chromedriver')
    #Windows
    driver = wd.Chrome('C:/Yoo/git/cs411/yelp_scraper/chromedriver.exe')
    driver.get(url)
    jsonlist = []
    f = open('yelp_cu_place.json', 'a+')
    f.write('[')

    for j in range(30):
        nitems = len(driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]').find_elements_by_xpath('li[@class="regular-search-result"]'))
        for i in range(nitems):
            dic = {}
            while (1):
                try:
                    pagelist = driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]')
                    result = pagelist.find_elements_by_xpath('li[@class="regular-search-result"]')[i]
                    imageurl = result.find_element_by_tag_name("img").get_attribute("src")
                    dic['imageurl'] = str(imageurl)
                    item = result.find_element_by_class_name("js-analytics-click")
                    # item.click()
                    break
                except WebDriverException:
                    print('err')
                    pass

            driver.implicitly_wait(10)
            main_window = driver.current_window_handle
            item.send_keys(Keys.CONTROL + Keys.RETURN)
            windows = driver.window_handles
            driver.switch_to.window(windows[1])
            dic["title"] = driver.find_element_by_class_name("biz-page-title").text
            dic["category"] = "Things to do"
            dic["addr"] = str(driver.find_element_by_class_name("street-address").text.replace('\n',' '))
            dic["city"] = "Urbana Champaign, IL"
            try:
                rating = driver.find_element_by_class_name("rating-very-large").get_attribute("title")
                dic["rating"] = str(re.search(r'\d.\d', rating).group(0).strip())
            except NoSuchElementException:
                dic["rating"] = "N/A"
            try:
                table = driver.find_element_by_class_name("hours-table")
                for i in range(1, 8):
                    hours = str(table.find_element_by_xpath("tbody/tr["+str(i)+"]/td[1]").text)
                    if len(hours.strip()) > 8:
                        break

            except NoSuchElementException:
                hours = "N/A - N/A"

            dic["hours"] = hours

            geo = json.loads(driver.find_element_by_class_name("lightbox-map").get_attribute("data-map-state"))
            try:
                lat = geo['center']['latitude']
                lon = geo['center']['longitude']

            except e:
                lat = 'N/A'
                lon = 'N/A'

            dic["lat"] = lat
            dic["lon"] = lon
            print(dic)
            jsonlist.append(dic)
            f.write("{0},".format(str(dic)))
            # driver.back()
            driver.close()
            driver.switch_to_window(main_window)

        driver.implicitly_wait(10)
        next = driver.find_element_by_xpath("//a[@class='u-decoration-none next pagination-links_anchor']")

        while(1):
            try:
                next.click()
                break
            except WebDriverException:
                print("err", j)
                pass

        driver.implicitly_wait(10)

    with open('yelp_cu_place.json', 'w') as fp:
        json.dump(jsonlist, fp)


    driver.close()
    print("CU PLACE DONE")


CU_PLACE()
