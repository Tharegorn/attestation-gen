from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import json
import datetime
from datetime import datetime


def insert(id, value, driver):
    elem = driver.find_element_by_name(id)
    elem.clear()
    elem.send_keys(value)

def web(av, reason):
    now = datetime.now()
    with open("profiles/" + av.lower() + ".json") as json_file:
        data = json.load(json_file)
        first = data["prenom"]
        last = data["nom"]
        date = data["datenaissance"]
        place = data["lieunaissance"]
        add = data["adresse"]
        city = data["ville"]
        code = data["codepostal"]
    driver = webdriver.Firefox()
    driver.get("https://media.interieur.gouv.fr/deplacement-covid-19/")
    insert("firstname", first, driver)
    insert("lastname", last, driver)
    insert("birthday", date, driver)
    insert("placeofbirth", place, driver)
    insert("address", add, driver)
    insert("city", city, driver)
    insert("zipcode", code, driver)
    insert("heuresortie", now.strftime("%H:%M"), driver)
    elem = driver.find_element_by_id("checkbox-" + reason)
    elem.click()
    elem = driver.find_element_by_id("generate-btn")
    elem.click()
    assert "No results found." not in driver.page_source
