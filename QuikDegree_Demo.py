#Quik Degree FrameWork - Franklin College of Arts and Sciences
#Author: Faisal Hossain


""" TO DO LIST:
- Double Major
- Multiple Minors
"""

from tkinter import *

#Init
root = Tk()
root.minsize(170, 240) #Minium Window Size
root.title("Quik Degree")

#Reponsive Sizing
for x in range(4):
    root.columnconfigure(x, weight=1)

for y in range(7):
    root.rowconfigure(y, weight=1)
    
#Title
title = Label(root,text="Quik Degree",anchor=CENTER).grid(row=1,column=0,columnspan=2,sticky=NSEW)

#University
univText = Label(root,text="University:").grid(row=2,column=0,sticky=W)
univOptions = StringVar(root)
univOptions.set("                                   ") # default value
univMenu = OptionMenu(root, univOptions, "University of Georgia")
univMenu.grid(row=2,column=1,sticky=W)

#College
univText = Label(root,text="College:").grid(row=3,column=0,sticky=W)
collegeOptions = StringVar(root)
collegeOptions.set("                                   ") # default value
collegeMenu = OptionMenu(root, collegeOptions, "Franklin College of Arts & Sciences")
collegeMenu.grid(row=3,column=1,sticky=W)

#Major
majorText = Label(root,text="Major:").grid(row=4,column=0,sticky=W)
majorOptions = StringVar(root)
majorOptions.set("                                   ") # default value
majorMenu = OptionMenu(root, majorOptions, "Computer Science")
majorMenu.grid(row=4,column=1,sticky=W)

#Area of Emphasis
AEText = Label(root,text="Area of Emphasis:").grid(row=5,column=0,sticky=W)
AEOptions = StringVar(root)
AEOptions.set("                                   ") # default value
AEMenu = OptionMenu(root, AEOptions, "Data Science")
AEMenu.grid(row=5,column=1,sticky=W)

#Minor
minorText = Label(root,text="Minor:").grid(row=6,column=0,sticky=W)
minorOptions = StringVar(root)
minorOptions.set("                                   ") # default value
minorMenu = OptionMenu(root, minorOptions, "Mathematics")
minorMenu.grid(row=6,column=1,sticky=W)

#Certificate
certText = Label(root,text="Certificate:").grid(row=7,column=0,sticky=W)
certOptions = StringVar(root)
certOptions.set("                                   ") # default value
certMenu = OptionMenu(root, certOptions, "Data Science")
certMenu.grid(row=7,column=1,sticky=W)

#Next Button
#Check out: https://pythonprogramming.net/change-show-new-frame-tkinter/

root.mainloop()

