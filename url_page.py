from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://selenium-blog.herokuapp.com/articles/new')

ids = driver.find_elements_by_xpath('//*[@id]')
for id in ids:
    #print ii.tag_name
    print ( id.get_attribute('id') )

title = "This is title 2"
description = "This is description for title 3"

def article_title(title):
      field = driver.find_element_by_id('article_title')
      field.send_keys(title)
def article_description(description):
      field = driver.find_element_by_id('article_description')
      field.send_keys(description)

def new_article():
    new_article_click = driver.find_element_by_name('commit')
    new_article_click.click()

article_title(title)
article_description(description)
new_article()
