# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:56:16 2021

@author: Diego Garcia
"""

from selenium import webdriver
import pandas as pd
import time

class EstateAgent:
    links = []
    company_name = []
    address = []
    phone = []
    website = []
    socialmedia = []
    n_rent = []
    n_sale = []
    avg_price = []
    avg_rent = []
    df = pd.DataFrame()
    
    
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.GetWebsite()
        self.GetLinks()
        self.GetData()
        self.dataframe()
    
    def GetWebsite(self):
        self.browser.get('https://www.primelocation.com/find-agents/estate-agents/directory/a/')
        time.sleep(3)
    
    def GetLinks(self):
        x = self.browser.find_element_by_xpath('//div[@class="agents-az"]')
        links = x.find_elements_by_tag_name('a')
        condition = lambda link: '.com/find-agents/estate-agents/company' in link.get_attribute('href')
        valid_links = list(filter(condition,links))
            
        for i in range(len(valid_links)):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
    
    def GetData(self):
        for index,link in enumerate(self.links):
            self.browser.get(link)
            time.sleep(3)
            
            self.getName()
            time.sleep(1)
            
            self.getAddress()
            time.sleep(1)
            
            self.getNumber()
            time.sleep(1)
            
            self.getWebsite()
            time.sleep(1)
            
            self.getProperties()
            time.sleep(1)
            
            
            if index == 3:
                break
            
    def getName(self):
        x = self.browser.find_element_by_xpath('//div[@class="agents-results"]')
        name = x.find_element_by_tag_name('h2').find_element_by_tag_name('a')
        company_name = name.get_attribute('innerHTML')
        self.company_name.append(company_name)
        print(company_name)
        
        name.click()
    
    def getAddress(self):
        x = self.browser.find_element_by_xpath('//div[@class="sidebar sbt"]')
        firstfilter = x.find_element_by_tag_name('p').find_element_by_tag_name('span')
        address = firstfilter.get_attribute('innerHTML')
        print(address)
        self.address.append(address)
    
    def getNumber(self):
        x = self.browser.find_element_by_xpath('//div[@class="sidebar sbt"]')
        firstfilter = x.find_element_by_xpath('//span[@class="agent_phone"]').find_element_by_tag_name('a')
        number = firstfilter.get_attribute('href')
        self.phone.append(number)
        print(number)
    
    def getWebsite(self):
        search = self.browser.find_elements_by_tag_name('h5')
        substring = 'Visit'
        substring2 = 'Follow'
        
        if len(search)>1:
            website=''
            media = ''
            for i in range(0,len(search)):
                string=search[i].text
                if substring in string:
                    website=search[i].find_element_by_tag_name('a').get_attribute('href')
                    print(website)
                
                if substring2 in string:
                    social= self.browser.find_element_by_xpath('//div[@class="social-media-share-buttons agent"]')
                    media = social.find_element_by_tag_name('a').get_attribute('href')
                    print(media)
                    
            if bool(website)==True:
                self.website.append(website)
            else:
                self.website.append('Nan')
            if bool(media)==True:
                self.socialmedia.append(media)
            else:
                self.socialmedia.append('Nan')
        
        else:
            self.website.append('Nan')
            self.socialmedia.append('Nan')
    
    def getProperties(self):
        search = self.browser.find_elements_by_xpath('//table[contains(@class,"stripe")]')
        substring = 'sale'
        substring2 = 'rent'
        
        if len(search)>0:
            n_sale=''
            rent=''
            avg_price=''
            avg_rent=''
            search2=search[0].find_elements_by_tag_name('tr')
            for i in range(1,len(search2)):
                string = search2[i].find_element_by_tag_name('td').text
                if substring in string:
                    n_sale = search2[i].find_element_by_xpath('//td[@class="center"]').text
                    avg_price = search2[i].find_element_by_xpath('(//td[@class="center"])[2]').text
                    print(n_sale)
                    print(avg_price)

                if substring2 in string:
                    j = i+1
                    rent = search2[i].find_element_by_xpath('//*[@id="tab-overview"]/table/tbody/tr[{}]/td[2]'.format(j)).text
                    avg_rent = search2[i].find_element_by_xpath('//*[@id="tab-overview"]/table/tbody/tr[{}]/td[3]'.format(j)).text
                    print(rent)
                    print(avg_rent)
                    
            if bool(n_sale)==True:
                self.n_sale.append(n_sale)
            else:
                self.n_sale.append('Nan')
            if bool(rent)==True:
                self.n_rent.append(rent)
            else:
                self.n_rent.append('Nan')
            if bool(avg_price)==True:
                self.avg_price.append(avg_price)
            else:
                self.avg_price.append('Nan')
            if bool(avg_rent)==True:
                self.avg_rent.append(avg_rent)
            else:
                self.avg_rent.append('Nan')
        
        else:
            self.n_sale.append('Nan')
            self.n_rent.append('Nan')

    def dataframe(self): 
        self.df = pd.DataFrame(list(zip(self.company_name,self.address,self.phone,self.website,self.socialmedia,
                                   self.n_sale,self.avg_price,self.n_rent,self.avg_rent)), 
               columns =['Company', 'Address','Phone','Website','Social Media','N° for Sale','Avg Price','N° for Rent',
                         'Avg Price Rent'])
                
        

realstate = EstateAgent()


        
        