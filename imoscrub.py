#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:08:59 2019

@author: adam
"""

import requests
from bs4 import BeautifulSoup

link = 'http://imo-official.org/year_individual_r.aspx?year=1990'

page = requests.get(link).text
soup = BeautifulSoup(page, 'lxml')
table = soup.find_all('table')
contestants = table[0].findAll('tr')

for contestant in contestants[2:]:
    scoreline=contestant.getText().split()
