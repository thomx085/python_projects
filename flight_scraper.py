# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:42:14 2023

@author: Tanner
"""

import time, smtplib, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from email.message import EmailMessage


class flight_scraper():
    def __init__(self):

        #setting the selenium configuration
        self.exec_path = r'C:\python\extensions\chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=C:\\AppData\\Local\\Google\\Chrome\\User Data')
        
        #setting the email configuration
        self.login = ('my_email', 'passkey')
        self.from_email = 'my_email'
        self.to_list = ['my_email', 'martis_email', 'elliots_email']
        self.subject = 'Todays top 10 Cheapest Flights to Pittsburgh'

    def scrape_and_send(self):   
        
        #setting the driver
        driver = webdriver.Chrome(executable_path=self.exec_path, options=self.options)
        
        #going to the webpage
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
        
        #setting the date and going to the flights
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
        
        #closing out the web navigator
        driver.quit()
        
        #initializing the email settings
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.login)
        
        #composing the email
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.from_email
        msg['To'] = self.to_list
        msg.set_content(f'\nFlight 1: \n {flights[0]} \nFlight 2: \n {flights[1]} \nFlight 3: \n {flights[2]} \nFlight 4: \n {flights[3]} \nFlight 5: \n {flights[4]} \
            \nFlight 6: \n {flights[5]} \nFlight 7: \n {flights[6]} \nFlight 8: \n {flights[7]} \nFlight 9: \n {flights[8]} \nFlight 10: \n {flights[9]} \
                \n \n Please note this is an automated summary so dont kill the snek (python)')
        
        #sending the message
        s.send_message(msg)
        s.quit()
        
def main():
    
    #start time
    start_time = time.time()
    
    #setting the local config
    c = flight_scraper()
    
    #calling the function
    c.scrape_and_send()
    
    #end time
    end_time = time.time() - start_time
    print('Report sent, time elapsed: ' + str(round(end_time,0/60) + 'minutes.'))
    
#running from batch
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    
    
    





