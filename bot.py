#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+           Python Module : Bot.py
#+   Contains Function :
#                     startBot - takes 3 parameter :-
#+
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def startBot(username,password,url):
    # specifying the path to the Chrome web driver into a variable
    #path = "C:\\Users\\Sarika Sah\\Downloads\\chrome-win64\\chrome-win64"

    #passing the path to the Selenium web driver
    driver = webdriver.Chrome()

    # passing the value of url into the druver to open it
    driver.get(url)

   
    driver.find_element(By.ID , "user_email").send_keys(username)
    driver.find_element(By.ID, "user_password").send_keys(password)

    #clicking the submitting button
    driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

    # credentials for login in

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

