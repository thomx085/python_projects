# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:42:14 2023

@author: Tanner
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import os
import time
import smtplib
from email.message import EmailMessage

exec_path = r'C:\Users\Tanner\Desktop\python\extensions\chromedriver.exe'

os.system('taskkill /im chrome.exe /f')

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Tanner\\AppData\\Local\\Google\\Chrome\\User Data')
# options.add_argument('headless')

driver = webdriver.Chrome(executable_path=exec_path, options=options)
action = ActionChains(driver)

driver.get('https://www.expedia.com/Flights') 
time.sleep(5)

#origin plan
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div/div/div[1]/button"))).click()
origin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/section/div/div[1]/div/input')))
origin.send_keys('MSP')
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/section/div/div[2]/div/ul/li[1]/div/button"))).click()

#destination plan
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/button"))).click()
destination = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/section/div/div[1]/div/input')))
destination.send_keys('PIT')
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/section/div/div[2]/div/ul/li[1]/div/button"))).click()

#setting the date
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/button[1]'))).click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/button[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/button[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/button[2]').click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[4]/button'))).click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[1]/button'))).click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/button'))).click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/form/div[3]/div/button'))).click()

#number of flights to look into
flight_list = ['1','2','3','4','5','6','7','8','9','10']

#empty flight list to append to
flights = []

#looping through the top 10 cheapest flights
for flight_number in flight_list:
    temp_flight_details = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[' + flight_number + ']/div/div/div/button'))).text
    temp_flight_details = temp_flight_details.replace('Select and show fare information for', '')
    flights.append(temp_flight_details)
    
driver.quit()

#initializing the email settings
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('tannerthom22@gmail.com', 'zpbekvqeoiejkpzw')

#composing the email
msg = EmailMessage()
msg['Subject'] = 'Todays top 10 Cheapest Flights to Pittsburgh'
msg['From'] = 'tannerthom22@gmail.com'
msg['To'] = ['tannerthom22@gmail.com', 'martitschida@gmail.com', 'elliotmusielewicz@gmail.com']
msg.set_content(f'\nFlight 1: \n {flights[0]} \nFlight 2: \n {flights[1]} \nFlight 3: \n {flights[2]} \nFlight 4: \n {flights[3]} \nFlight 5: \n {flights[4]} \
    \nFlight 6: \n {flights[5]} \nFlight 7: \n {flights[6]} \nFlight 8: \n {flights[7]} \nFlight 9: \n {flights[8]} \nFlight 10: \n {flights[9]} \
        \n \n Please note this is an automated summary so dont kill the snek (python)')

#sending the message
s.send_message(msg)
s.quit()









#get prices
# price1 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[1]/div/div/div/button'))).text
# print(price1)

# price2 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[2]/div/div/div[1]/button'))).text
# print(price2)

# price3 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[3]/div/div/div[1]/button'))).text
# print(price3)

# price4 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[4]/div/div/div[1]/button'))).text
# print(price4)

# price5 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div[1]/section/main/ul/li[5]/div/div/div[1]/button'))).text
# print(price5)




# //*[@id="AQruAQrYAXY1LXNvcy03Yjc5YmU1ZTgxZjZmYzZjMzQ3MGFkNjM3NDk2ZWIyMC0wLTAtMX4yLlN-QVFvQ0NBRVNCd2pVQkJBQkdBRW9BbGdDY0FBfkFRb2pDaUVJMDdJQkVnUXhNRFV6R014OElJLWFBU2pBNExNQ01MRGhzd0k0VTBBQVdBRUtJd29oQ05PeUFSSUVNVEExTkJpUG1nRWd6SHdveW9PMEFqREtoTFFDT0ZOQUFGZ0JFZ29JQVJBQkdBRXFBbE5aR0FFaUJBZ0JFQUVvQWlnREtBUXdEURGamZmZmVlnQCIBASoFEgMKATESPwoWCgoyMDIzLTA4LTAzEgNNU1AaA1BJVAoWCgoyMDIzLTA4LTA2EgNQSVQaA01TUBIHEgVDT0FDSBoCEAEgAg=="]/div/div/div/div/div[1]/div[2]/div/div/section/span[2]
# //*[@id="AQruAQrYAXY1LXNvcy03Yjc5YmU1ZTgxZjZmYzZjMzQ3MGFkNjM3NDk2ZWIyMC0wLTAtMX4yLlN-QVFvQ0NBRVNCd2pVQkJBQkdBRW9BbGdDY0FBfkFRb2pDaUVJMDdJQkVnUXhNRFV6R014OElJLWFBU2pBNExNQ01MRGhzd0k0VTBBQVdBRUtJd29oQ05PeUFSSUVNVEExTkJpUG1nRWd6SHdveW9PMEFqREtoTFFDT0ZOQUFGZ0JFZ29JQVJBQkdBRXFBbE5aR0FFaUJBZ0JFQUVvQWlnREtBUXdEURGamZmZmVlnQCIBASoFEgMKATESPwoWCgoyMDIzLTA4LTAzEgNNU1AaA1BJVAoWCgoyMDIzLTA4LTA2EgNQSVQaA01TUBIHEgVDT0FDSBoCEAEgAg=="]/div/div/div/button/span/text()






# date_element = driver.find_element(By.ID, 'date_form_field')
# driver.execute_script("arguments[0].setAttribute('value', '2023-08-03 - 2023-08-07')", date_element)




# print(str(para_element))

# driver.execute_script('document.getElementById("date_form_field").appendChild(document.createElement("a"))')
# element = driver.find_element(By.TAG_NAME, 'a')
# driver.execute_script("arguments[0].setAttribute('value', '2023-08-03 - 2023-08-06')", element)
# driver.execute_script("var ele=arguments[0]; ele.innerHTML = '2023-04-03 - 2023-04-04';", element)






