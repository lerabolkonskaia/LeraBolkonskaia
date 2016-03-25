# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import selenium_fixture import driver

    def test_adding(app):
        app.go_to_home_page()
        app.login (User.Admin())
        app. adding_movie (driver)
        assert app.movie_is_added()
        adding_negmovie (driver)
        assert app.movie_is_not_added
        logout (driver)


    


        


