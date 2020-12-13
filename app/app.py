from collections import Counter
from time import sleep
from datetime import datetime
from random import randrange

from selenium import webdriver

target_url = "https://hh.kz/search/vacancy?area=160&fromSearchLine=true&st=searchVacancy&text=Python&from=suggest_post"

def main():
    chromedriver_path = "../webdriver/chromedriver_86.0.4240.22/chromedriver"
    try:
        driver = webdriver.Chrome(chromedriver_path)

        driver.get(target_url)
        # div[@class='vacancy-serp-item ']//
        vacancies = driver.find_elements_by_xpath("//span[@class='g-user-content']//a")

        urls = []
        for i in vacancies:
            a = i.get_attribute('href')
            url = {
                'href': a
            }
            urls.append(url)
    
        plates = []
        count = 0
        for j in urls:
            sleep(randrange(2, 8))
            print(datetime.now())

            driver.get(j['href'])
            plate_tags = driver.find_elements_by_class_name("bloko-tag__section_text")
            plate_elements = []
            for p in plate_tags:
                plates.append(p.text.strip())
            
            count += 1
            if count > 2:
                break
            
        print(Counter(plates).most_common(10))

    finally:
        driver.quit()

if __name__ == '__main__':
    main()