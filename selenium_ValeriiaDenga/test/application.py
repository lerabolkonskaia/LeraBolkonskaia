from selenium import webdriver
import pytest

class Application (object):
	def __init__(self, driver):
		self.driver= driver
		self.base_url = base_url
		self.wait = WebDriverWait (driver, 10)

def go_to_home_page (self):
	self.driver.get (self.base_url) 

def login (self, user):
	    driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()

def logout (self):
	    driver = self.driver
        driver.find_element_by_link_text("Logout").click()
        driver.switch_to_alert().accept()

def adding_movie (self):
	    driver = self.driver
        driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys(movie.imdbid)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie.name)
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys(movie.aka)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys(movie.year)
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys(movie.duration)
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys(movie.rating)
        driver.find_element_by_id("cover").clear()
        driver.find_element_by_id("cover").send_keys("https://github.com/lerabolkonskaia/LeraBolkonskaia/blob/master/selenium_ValeriiaDenga/test/aTJ8esL3idQ%20(1).jpg")
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys(movie.text_languages_0)
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys(movie.subtitles)
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("audio").send_keys(movie.audio)
        driver.find_element_by_name("video").clear()
        driver.find_element_by_name("video").send_keys(movie.video)
        driver.find_element_by_name("country").clear()
        driver.find_element_by_name("country").send_keys(movie.country)
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text("Home").click()

def adding_negmovie(self):
		driver = self.driver
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

def search(self):
		driver = self.driver
        driver.find_element_by_name("submit").click()
        driver.find_element_by_xpath("//a[@id='sort-button']/span[2]").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("2015")
        driver.find_element_by_id("q").send_keys(Keys.ENTER)

def search_neg (self):
		driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("2016")
        driver.find_element_by_id("q").send_keys(Keys.ENTER)

def deleting (self):
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_css_selector("img[alt=\"Cold Heart\"]").click()
        driver.find_element_by_link_text("Remove").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")

def movie_is_added (self):
	driver = self.driver
	try:
		self.wait.until (presence_of_element_located ((By.CSS_SELECTOR, "h2")))
		return True
	except WebdriverException:
		return False

def movie_is_not_added (self):
	driver = self.driver
	try:
		self.wait.until (presence_of_element_located ((By.CSS_SELECTOR, "css=#updateform > table.3.1 This field is required")))
		return True
	except WebdriverException:
		return False

def movie_is_found (self):
	driver = self.driver
	try:
		self.wait.until (presence_of_element_located ((By.CSS_SELECTOR, "img[alt=\"Frozen\"]")))
		return True
	except WebdriverException:
		return False

def movie_is_not_found (self):
	driver = self.driver
	try:
		self.wait.until (presence_of_element_located ((By.CSS_SELECTOR, "No movies where found.")))
		return True
	except WebdriverException:
		return False

def movie_is_deleted (self):
	driver = self.driver
	try:
		self.wait.until (presence_of_element_located ((By.CSS_SELECTOR, "h1")))
		return True
	except WebdriverException:
		return False