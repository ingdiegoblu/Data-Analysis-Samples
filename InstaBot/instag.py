# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:03:25 2020

@author: Diego Garcia
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

class InstaG:
    username= '' #insert your username
    password= '' #insert your password
    hashtags = [
        'sunset_vision','landscape','sunsetshots','sunsetlovers',
    ] #insert a list of hashtags
    
    comments = [
        'WooW', 'Amazing Work!', 'Your posts are amazing!', 'Nice!','Really Cool!',
        'Tooop!!!','Awesome!', 'Well done', 'Keep Going!','Super Cool!',
         ] # insert comments
    
    links = []
    
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.login()
        self.hustle()
    
    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)

        username_field=self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(2)
        
        password_field=self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(2)
        
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(2)
    
    def hustle(self):
        self.getTopPosts()
        self.execute()
        self.finalize()

    
    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
            time.sleep(2)
            
            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            
            for i in range(0,5):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)
                    
    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(1)
            
            self.browser.execute_script("window,scrollTo(0,120);")
            time.sleep(1)
            
            self.comment()
            time.sleep(1)
            
            self.like()
            
            sleeptime = random.randint(18,30)
            time.sleep(sleeptime)
            
    def comment(self):
        comment_input= lambda: self.browser.find_element_by_tag_name('textarea')
        comment_input().click()
        comment_input().clear()
        
        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1,7)/30
            time.sleep(delay)
        
        comment_input().send_keys(Keys.RETURN)
        
    def like(self):
        LIKE_BUTTON_PATH = '(//button[@class="wpO6b "])[2]'
        self.browser.find_element_by_xpath(LIKE_BUTTON_PATH).click()
    
    def finalize(self):
        self.browser.close()
        sys.exit()
        
        
instagram = InstaG()