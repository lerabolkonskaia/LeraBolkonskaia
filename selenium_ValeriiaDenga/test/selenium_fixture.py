from selenium import webdriver
import pytest


@pytest.fixture (scope = "module")
def app (request):
	driver = webdriver.Firefox()
	driver.implicitly_wait (10)
	request.addfinalizer(driver.quit)
	return Application (driver)
