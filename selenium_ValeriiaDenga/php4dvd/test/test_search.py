# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost//php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_search(self):
        driver = self.driver
        driver.find_element_by_name("submit").click()
        driver.find_element_by_xpath("//a[@id='sort-button']/span[2]").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("2015")
        driver.find_element_by_id("q").send_keys(Keys.ENTER)
        try: self.assertEqual("No movies where found.", driver.find_element_by_css_selector("div.content").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("2016")
        driver.find_element_by_id("q").send_keys(Keys.ENTER)
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Frozen\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
    
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
