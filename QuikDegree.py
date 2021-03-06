#Quik Degree - Franklin College of Arts and Sciences
#Author: Faisal Hossain

#Currently, demo is set to work only for UGA's CS major requirements

# Import libraries
import requests
import urllib.request
import time
#import mysql.connector #MySQL
from bs4 import BeautifulSoup
"""
#MySQL Init
config = {
  'user': 'faisalhossain',
  'password': 'F@1sal75',
  'host': 'localhost',
  'database': 'TestDB',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
cursor.execute('SELECT * FROM TestDB.dbo.Person')
 
for row in cursor:
    print(column)
"""

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
for a in start1.find_all('a'):
    degreeReq[a.string] = ['https://osas.franklin.uga.edu/' + a.get('href')]

del degreeReq['Foreign Language Requirement\xa0'] 
for k,v in degreeReq.items():
    print (k)
    print (v)
    print()

# College Degree Requirements Sub
print('sub start')
for k, v in degreeReq.items():
    url = v[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    start = soup.find('tbody') #find first html <tbody>

    for h3 in start.find_all('h3'):
        print(h3.string)
        print("Course Codes:")
        for a in start.find_all('a'):
            print(a.string)
            if start.find('h3'):
                break

    print("[][] END [][]")
    
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


print("[] After ------------")
for k,v in degreeReq.items():
    print (k)
    print (v)
    print()


#for x in degreeReq:
#    print (x)
##    for y in cars[x]:
##        print (y,':',cars[x][y])


cursor.execute('''
                INSERT INTO TestDB.dbo.Person (Name, Age, City)
                VALUES
                ('Bob',55,'Montreal'),
                ('Jenny',66,'Boston')
                ''')
conn.commit()


"""
Useful links:
https://stackoverflow.com/questions/44290485/beautiful-soup-error-nonetype-object-and-if?rq=1
https://stackoverflow.com/questions/4362981/beautifulsoup-how-do-i-extract-all-the-lis-from-a-list-of-uls-that-contains
"""
cnx.close()
