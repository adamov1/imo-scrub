#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:46:11 2019

@author: adamov1
"""

import imoscrub

def ravi(scoreline):
    return sum((int(i)-4)*(int(i)-4) for i in scoreline)

def minimum_ravi_index(first_year, last_year):
    minimum=10000
    minrow=[]
    minyear = 0
    
    for year in range(first_year, last_year+1):
        for row in imoscrub.scores_from_year(year):
            if len(row)<8:
                continue
            row_ravi = ravi(row[2:8])
            if row_ravi<minimum:
                minimum=row_ravi
                minrow=row
                minyear=year
    return minimum, minyear, minrow

def ravi_of_person(name):
    minimum=10000

    for row in imoscrub.scores_from_person(name):
        if len(row)<8:
            continue
        row_ravi = ravi(row[2:8])
        if row_ravi<minimum:
            minimum=row_ravi
    return minimum
