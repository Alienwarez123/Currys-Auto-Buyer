import selenium
import config
import requests
import discord_webhook
from discord_webhook import DiscordWebhook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
timeout = config.sitetimeout
discordmention = config.discordmention
discordwebhook = config.discordwebhook
# Using Chrome to access web
driver = webdriver.Chrome("chromedriver.exe")
# Open the website


driver.get("https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/asus-geforce-rtx-3070-8-gb-dual-oc-graphics-card-10215776-pdt.html")
try: #Cookies
    element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
    WebDriverWait(driver, 1).until(element_present)
    driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
except TimeoutException:
    print("Timed out waiting for page to load")


while True:
    for z in config.sitelink2:
        driver.get(z) #GETS THE MAIN PAGE
        time.sleep(1)
        try: #CLICKS ADD TO BASKET
            element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="product-actions"]/div[4]/div[1]/button'))
            WebDriverWait(driver, 2).until(element_present)
            driver.find_element_by_xpath('//*[@id="product-actions"]/div[4]/div[1]/button').click()
            time.sleep(1)
            driver.get('https://www.currys.co.uk/app/basket')
            timeout = 0.001
            x = 0
            while x == 0:
                try: #CLICKS CHECKOUT
                    element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div/button/div'))
                    WebDriverWait(driver, timeout).until(element_present)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[2]/div/button/div').click()
                    x = 1
                except TimeoutException:
                    print("Timed out waiting for page to load")
                    try: #CLICKS CHECKOUT
                        element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div/button/div/span[2]'))
                        WebDriverWait(driver, timeout).until(element_present)
                        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div/button/div/span[2]').click()
                        x = 1
                    except TimeoutException:
                        print("Timed out waiting for page to load")
                        try: #CLICKS CHECKOUT
                            element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/button/span[2]'))
                            WebDriverWait(driver, timeout).until(element_present)
                            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/button/span[2]').click()
                            x = 1
                        except TimeoutException:
                            print("Timed out waiting for page to load")
            timeout = config.sitetimeout
            webhook = DiscordWebhook(url=discordwebhook, content=f"Autominer has got a graphics card {discordmention}")
            response = webhook.execute()

            time.sleep(1)


            try: #CLICKS delivery
                element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="delivery_location"]/input'))
                WebDriverWait(driver, timeout).until(element_present)
                postcode = driver.find_element_by_xpath('//*[@id="delivery_location"]/input')
            except TimeoutException:
                print("Timed out waiting for page to load")

            postcode.click()
            postcode.clear()
            postcode.send_keys(config.postcodefirst)
            time.sleep(0.70)
            postcode.send_keys(config.postcodelastdigit)
            time.sleep(1)
            postcode.send_keys(Keys.RETURN)

            time.sleep(0.30)
            try: #clicks free delivery
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div/div[3]/div[1]/button'))
                WebDriverWait(driver, timeout).until(element_present)
                driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]/div[2]/div/div[3]/div[1]/button').click()
            except TimeoutException:
                print("Timed out waiting for page to load")


            try: #clicks email
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input'))
                WebDriverWait(driver, timeout).until(element_present)
                driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input').click()
            except TimeoutException:
                print("Timed out waiting for page to load")

            email = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input')

            email.send_keys(config.emailaddress)
            email.send_keys(Keys.RETURN)


            try: #clicks password
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/input'))
                WebDriverWait(driver, timeout).until(element_present)
                driver.find_element_by_xpath('//*[@id="password"]/div[1]/input').click()
            except TimeoutException:
                print("Timed out waiting for page to load")

            password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/input')

            password.send_keys(config.curryspassword)
            password.send_keys(Keys.RETURN)

            try: #clicks postcode
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="addresses"]/div[2]/div[6]/div[1]/div/input'))
                WebDriverWait(driver, 5).until(element_present)
                driver.find_element_by_xpath('//*[@id="addresses"]/div[2]/div[6]/div[1]/div/input').click()
                password = driver.find_element_by_xpath('//*[@id="addresses"]/div[2]/div[6]/div[1]/div/input')
                time.sleep(0.5)
                password.clear()
                for x in range(0, 9):
                    password.send_keys(Keys.BACKSPACE)

                password.send_keys(config.postcodefirst+config.postcodelastdigit)
                password = driver.find_element_by_xpath('//*[@id="addresses"]/div[2]/div[8]/input')
                password.send_keys(config.houseaddress)
                password = driver.find_element_by_xpath('//*[@id="addresses"]/div[2]/div[10]/input')
                password.send_keys(config.housecity)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                driver.find_element_by_xpath('//*[@id="addresses"]/button').click()
                time.sleep(1)
            except TimeoutException:
                print("Timed out waiting for page to load")

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(0.20)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            webhook = DiscordWebhook(url=discordwebhook, content=f"Autominer has got a graphics card in the basket menu {discordmention}")
            response = webhook.execute()
            try: #clicks card
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button'))
                WebDriverWait(driver, timeout).until(element_present)
                driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button').click()
            except TimeoutException:
                print("Timed out waiting for page to load")


            try: #clicks cardnumber
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="cardNumber"]'))
                WebDriverWait(driver, timeout).until(element_present)
                driver.find_element_by_xpath('//*[@id="cardNumber"]').click()
            except TimeoutException:
                print("Timed out waiting for page to load")
            cardnumber = driver.find_element_by_xpath('//*[@id="cardNumber"]')
            cardnumber.send_keys(config.cardnumber)
            cardnumber = driver.find_element_by_xpath('//*[@id="cardholderName"]')
            cardnumber.send_keys(config.cardholder)
            cardnumber = driver.find_element_by_xpath('//*[@id="expiryMonth"]')
            cardnumber.send_keys(config.cardmonth)
            cardnumber = driver.find_element_by_xpath('//*[@id="expiryYear"]')
            cardnumber.send_keys(config.cardyear)
            cardnumber = driver.find_element_by_xpath('//*[@id="securityCode"]')
            cardnumber.send_keys(config.cardcvv)
            webhook = DiscordWebhook(url=discordwebhook, content=f"Autobuyer has got a graphics card in the card menu {discordmention}")
            response = webhook.execute()
            try: #clicks cardnumber
                element_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]'))
                WebDriverWait(driver, timeout).until(element_present)
                #driver.find_element_by_xpath('//*[@id="submitButton"]').click()
            except TimeoutException:
                print("Timed out waiting for page to load")
            webhook = DiscordWebhook(url=discordwebhook, content=f"Autobuyer has bought a gpu {discordmention}")
            response = webhook.execute()
            input("failed")
        except TimeoutException:
            print("Out Of stock")


