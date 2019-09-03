#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:08:59 2019

@author: adamov1
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_scores(link):
    #gets table from link
    page = requests.get(link).text
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find_all('table')
    contestants = table[0].findAll('tr')
    
    scores = [contestant.get_text('|').split('|') for contestant in contestants]
    return scores

def scores_from_year(year):
    #format of rows: name, country, p1, p2, p3, p4, p5, p6, total, rank, medal
    link = 'http://imo-official.org/year_individual_r.aspx?year='+str(year)
    return get_scores(link)[1:] #first row is header

def scores_from_person(name):
    #CASE SENSITIVE
    #interacts with search bar using selenium, slower, returns first search result (if exists)
    #format of rows: year, country, p1, p2, p3, p4, p5, p6, total, rank, rel, medal
    browser = webdriver.Firefox()
    browser.get("http://imo-official.org/search.aspx")
    searchbar = browser.find_element_by_name("ctl00$CPH_Main$TextBox1")
    searchbar.send_keys(name)
    searchbar.send_keys(u'\ue007') #ENTER
    
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h3"))) #10 seconds is max wait
    
    try:
        link = browser.find_element_by_partial_link_text(name).get_attribute("href")
        browser.quit()
        return get_scores(link)[2:]
    except NoSuchElementException:
        print(name+' is not on imo-official')
        browser.quit()
        return []
    

    