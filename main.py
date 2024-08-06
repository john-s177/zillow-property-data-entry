import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
soup = BeautifulSoup(response.text , "html.parser")

prices = soup.find_all("span", class_ = "PropertyCardWrapper__StyledPriceLine")
addresses = soup.find_all("address")
links = soup.find_all("a", class_ = "StyledPropertyCardDataArea-anchor")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScCjx4of6uI_d1UdSicmKnHb9Yl7KkXvvQ-75NCMsgQMv6KYA/viewform")
time.sleep(5)  # Wait for the page to load

for i in range(len(prices)):
    # Find the input fields
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    # Fill in the input fields
    address_input.send_keys(addresses[i].get_text())
    price_input.send_keys(prices[i].get_text())
    link_input.send_keys(links[i].get("href"))

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(4)  # Wait for the form to submit

    # Click the 'Submit another response' button
    another_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_button.click()

    time.sleep(4)  # Wait for the new form to load

driver.quit()
