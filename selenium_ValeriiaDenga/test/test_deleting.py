# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import selenium_fixture import driver

def test_deleting (driver):
    app.go_to_home_page()
    app.login (User.Admin())driver.get("http://localhost/php4dvd/")
    deleting (driver)
    assert app.movie_is_deleted
    logout(driver)

