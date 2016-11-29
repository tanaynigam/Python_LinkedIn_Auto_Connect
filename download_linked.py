from selenium import webdriver
import time

chromedriver = webdriver.Chrome(executable_path = 'C:\chromedriver_win32\chromedriver.exe')

def login_linkedin(): #email, password):

	url = 'https://www.linkedin.com/'

	chromedriver.get(url)

	#print chromedriver.page_source

	email = chromedriver.find_element_by_xpath('//*[@id="login-email"]')
	email.send_keys('tanaynigam12@gmail.com')

	password = chromedriver.find_element_by_xpath('//*[@id="login-password"]')
	password.send_keys('beaxtx.1993')

	sign_in = chromedriver.find_element_by_xpath('//*[@id="login-submit"]')
	sign_in.click()




time.sleep(2)

login_linkedin()#'tanaynigam12@gmail.com','beaxtx.1993')

search_input = chromedriver.find_element_by_xpath('//*[@id="main-search-box"]')
search_input.send_keys('technical recruiter')

search_button = chromedriver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
search_button.click()

time.sleep(2)

people_button = chromedriver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
people_button.click()

time.sleep(2)

connect_2nd = chromedriver.find_element_by_xpath('//*[@id="facet-N"]/fieldset/div/ol/li[3]/div/label/bdi')
connect_2nd.click()

time.sleep(2)

connect_button = chromedriver.find_elements_by_class_name('primary-action-button')
for a in connect_button:
	a.click()


time.sleep(10)
chromedriver.quit()