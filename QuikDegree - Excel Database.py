#Quik Degree - Franklin College of Arts and Sciences
#Author: Faisal Hossain

#Currently, demo is set to work only for UGA's CS major requirements

# Import libraries
import requests
import urllib.request
import time 
import xlwt #python3 -m pip install xlwt
from xlwt import Workbook 
from bs4 import BeautifulSoup

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

# Set the URL you want to webscrape from
url = 'https://osas.franklin.uga.edu/franklin-college-degree-requirements'
#url = 'http://bulletin.uga.edu/MajorsGeneral.aspx?MajorId=47'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

#College Degree Requirements
start = soup.find('article') #find first html <article>
start1 = start.find('ul') # find start of bulleted listed in article

degreeReq = {} #{College Requirement:[Link, Requirements....],}
counter = 0
for a in start1.find_all('a'):
    counter += 1
    degreeReq[a.string] = ['https://osas.franklin.uga.edu/' + a.get('href')]
    sheet1.write(counter, 0, a.string)

del degreeReq['Foreign Language Requirement\xa0'] #ERROR-Handling 
del degreeReq['History Requirement'] #ERROR-Handling 

for k,v in degreeReq.items():
    print (k)
    print (v)
    print()

# College Degree Requirements Sub
print('sub start')
counter1 = 0
counter2 = 0
for k, v in degreeReq.items():
    url = v[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    start = soup.find('tbody') #find first html <tbody>
    print()
    print("[||||||||||]" + k)
    counter1 += 1
    for a in start.find_all('a'): #Course
        counter2 += 1
        sheet1.write(counter1, counter2, a.string)

wb.save('xlwt example.xls')




# MISCELLANEOUS

""" WORKS 
    print("Course Headings:")
    for h3 in start.find_all('h3'):
        print(h3.string)
        v.append(h3.string)
    print("Course Codes:")
    for a in start.find_all('a'):
       print(a.string)
    print("[][] END [][]")
"""

    #a = soup.select_one('tbody a')
    #print(a)

#for x in degreeReq:
#    print (x)
##    for y in cars[x]:
##        print (y,':',cars[x][y])


"""
Useful links:
https://stackoverflow.com/questions/44290485/beautiful-soup-error-nonetype-object-and-if?rq=1
https://stackoverflow.com/questions/4362981/beautifulsoup-how-do-i-extract-all-the-lis-from-a-list-of-uls-that-contains
"""
