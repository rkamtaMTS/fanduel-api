# import packages
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# import custom packages

# define static variables

# define dynamic variables


class DRIVER:

	def __init__(self, browser_refresh_int, driver_headless, driver_location, url):
		self.browser_refresh_int = browser_refresh_int
		self.driver_headless = driver_headless
		self.driver_location = driver_location
		self.url = url

		# create webdriver instance
		# log initial time to track browser refresh requirement
		self.connect()
		self.browser_refresh_complete_time = time.time()


	# create webdriver instance
	def connect(self):

		# set headless attribute
		# set window size attribute to ensure consistency across devices
		options = Options()
		options.headless = self.driver_headless
		options.add_argument('window-size=1200,1100')

		# create webdriver object
		# navigate to webpage
		self.driver = webdriver.Chrome(self.driver_location, chrome_options=options)
		self.driver.get(self.url)


	# check internet connection
	def check_internet_connection(self):

		try:
			# attempt to access website
			requests.get(self.url, timeout=10)

		except:
			return False

		return True


	# refresh browser to ensure client-side continues updating webpage through API calls
	def browser_refresh(self):

		# refresh browser
		# log browser refresh completed time
		self.driver.refresh()
		print('Driver API Success: Refreshed Web Driver')
		self.browser_refresh_complete_time = time.time()


	# check if browser refresh is required
	def check_browser_refresh_required(self):

		# calculate time elapsed since driver creation or last refresh
		time_elapsed = time.time() - self.browser_refresh_complete_time

		# check if time elapsed is greater than browser refresh interval
		# refresh webpage
		if time_elapsed > self.browser_refresh_int:
			self.browser_refresh()

			return True

		return False


	def __repr__(self):

		return '{}'.format(vars(self))
