import json
from selenium import webdriver as wd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.yelp.com/search?find_desc=things+to+do&find_loc=Los+Angeles%2C+CA&ns=1"
#linux
# driver = wd.Chrome('/usr/bin/chromedriver')
#Windows
driver = wd.Chrome('C:/Yoo/git/cs411/yelp_scraper/chromedriver.exe')
driver.get(url)
jsonlist = []

for j in range(70):
    nitems = len(driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]').find_elements_by_xpath('li[@class="regular-search-result"]'))
    for i in range(nitems):
        dic = {}
        while (1):
            try:
                pagelist = driver.find_element_by_xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]')
                result = pagelist.find_elements_by_xpath('li[@class="regular-search-result"]')[i]
                item = result.find_element_by_class_name("js-analytics-click")
                item.click()
                break
            except WebDriverException:
                print('err')
                pass
        driver.implicitly_wait(10)
        dic["title"] = driver.find_element_by_class_name("biz-page-title").text
        dic["category"] = "Things to do"
        dic["addr"] = driver.find_element_by_class_name("street-address").text.replace('\n',' ')
        dic["city"] = "Los Angeles, CA"

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
        driver.back()

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

with open('yelp_la_place.json', 'w') as fp:
    json.dump(jsonlist, fp)


driver.close()
