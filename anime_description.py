from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path

site = 'https://animego.org/anime/magicheskaya-bitva-2-2332'


def anime_description(site):
    driver = wd.Chrome()
    driver.get(site)
    sleep(1)
    anime_title = driver.find_elements(By.CSS_SELECTOR, '.anime-title')
    title = anime_title[0].text.split('\n')
    descriprion_field_title = driver.find_elements(By.CSS_SELECTOR, '.col-6.col-sm-4')
    descriprions = driver.find_elements(By.CSS_SELECTOR, '.col-6.col-sm-8')
    res= {}
    for i in range(11):
        res[descriprion_field_title[i].text] = descriprions[i].text


    path = Path("desc.txt")
    with open(path,'w', encoding='utf-8') as file:
        file.write(f'{title[0]} \n\n')
        for key, val in res.items():
            file.write(f'{key} {val} \n')



anime_description(site)