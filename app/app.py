from collections import Counter
from time import sleep
from datetime import datetime
from random import randrange
from typing import List

from selenium import webdriver

CHROMEDRIVER_PATH = "../webdriver/chromedriver_86.0.4240.22/chromedriver"
TARGET_URL = "https://hh.kz/search/vacancy?area=160&fromSearchLine=true&st=searchVacancy&text={}&from=suggest_post"
MAX_ITERATION = 10
MIN_TIMEOUT = 2
MAX_TIMEOUT = 8

class HeadHunter():
    
    def __init__(self, search_word: str="Python", is_max_size: bool=False) -> None:
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        self.search_word = search_word
        self.is_max_size = is_max_size
    
    def run(self) -> None:
        try:
            urls = self.vacancies_list()
            skills = self.skill_list(urls)
        finally:
            self.driver.quit()
        
        print(Counter(skills).most_common(6))
    
    def vacancies_list(self) -> List:
        self.driver.get(TARGET_URL.format(self.search_word))
        vacancies_elements = self.driver.find_elements_by_xpath("//span[@class='g-user-content']//a")

        urls = []
        for i in vacancies_elements:
            a = i.get_attribute('href')
            url = {
                'href': a
            }
            urls.append(url)
        
        return urls

    def skill_list(self, urls:List) -> List:
        plates = []
        _len = len(urls)
        end = _len if self.is_max_size or MAX_ITERATION > _len else MAX_ITERATION
        for url in urls[:end]:
            self.pause()

            self.driver.get(url['href'])
            plate_tags = self.driver.find_elements_by_class_name("bloko-tag__section_text")
            for p in plate_tags:
                plates.append(p.text.strip())

        return plates
    
    def pause(self):
        sleep(randrange(MIN_TIMEOUT, MAX_TIMEOUT))
        print(datetime.now())

if __name__ == '__main__':
    parser = HeadHunter(is_max_size=True)
    parser.run()