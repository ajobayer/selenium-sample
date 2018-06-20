from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get('https://selenium-blog.herokuapp.com/login')

#email = "ajobayer@test.com"
email = "bad-email@test.com"
password = "password"
flash_success = "You have successfully logged in!"
flash_danger = "There was a problem logging in"

def enter_email_address(email):
  email_field = driver.find_element_by_id('session_email')
  email_field.send_keys(email)

def enter_password(password):
  password_field = driver.find_element_by_id('session_password')
  password_field.send_keys(password)

def log_in_form():
  log_in_button = driver.find_element_by_name('commit')
  log_in_button.click()

def get_banner_text():
    try:
        flash_success = driver.find_element_by_id('flash_success')
    except:
        print ("----Login failed------")
        try:
            flash_danger = driver.find_element_by_id('flash_danger')
            print(flash_danger.text)
        except:
            print("Could not find the flash_danger element!")

enter_email_address(email)
enter_password(password)
log_in_form()
get_banner_text()
