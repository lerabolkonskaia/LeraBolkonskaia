# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Tsk3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_tsk3(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("1234578")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Cold Heart")
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("Frozen")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2016")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("202")
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("2")
        driver.find_element_by_id("cover").clear()
        driver.find_element_by_id("cover").send_keys("C:\\Users\\LeraJ\\Desktop\\aTJ8esL3idQ (1).jpg")
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys("French, German, English")
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys("no")
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("audio").send_keys("good")
        driver.find_element_by_name("video").clear()
        driver.find_element_by_name("video").send_keys("excellent")
        driver.find_element_by_name("country").clear()
        driver.find_element_by_name("country").send_keys("USA")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Hispanic maniac")
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("Murderer")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("106")
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("3")
        driver.find_element_by_id("submit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | css=#updateform > table.3.1 | ]]
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("img[alt=\"Cold Heart\"]").click()
        driver.find_element_by_link_text("Remove").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
