from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://selenium-blog.herokuapp.com/signup')

#browser = webdriver.Chrome()
#browser.get('http://seleniumhq.org/')

import time
from datetime import datetime
now = datetime.now()

timestamp = (time.mktime(now.timetuple()))

username = "user"+str(int(timestamp))
email = "user"+str(int(timestamp))+"@test.com"
password = "password"
expected_banner_text = "Welcome to the alpha blog user"+str(int(timestamp))

def enter_username(username):
  username_field = driver.find_element_by_id('user_username')
  username_field.send_keys(username)

def enter_email_address(email):
  email_field = driver.find_element_by_id('user_email')
  email_field.send_keys(email)

def enter_password(password):
  password_field = driver.find_element_by_id('user_password')
  password_field.send_keys(password)

def submit_form():
  sign_up_button = driver.find_element_by_id('submit')
  sign_up_button.click()

def get_banner_text():
  banner = driver.find_element_by_id('flash_success')
  return banner.text


# Fill out and submit form
enter_username(username)
enter_email_address(email)
enter_password(password)
submit_form()
  # Confirm user is signed up successfully
banner_text = get_banner_text()

if(banner_text == expected_banner_text):
	print("Confirm user is signed up successfully")
else:
	print("This is not registered users")


