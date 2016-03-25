# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import selenium_fixture import driver

def test_adding(app):
    app.go_to_home_page()
    app.login (User.Admin())
    search (driver)
    assert app.movie_is_found
    search_neg (driver)
    assert app.movie_is_not_found
    logout(driver)

