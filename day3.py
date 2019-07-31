# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:33:39 2019

@author: STEM
"""


# example 1; listing numbers of chocolate
Darkchocolate = 5
Milk = 6
White = 8
print(White)

#example 2: creating variables for the number of chcolates only
def cadburyBox(cadbury1,cadbury2,cadbury3):
    print ("There are",cadbury1,"milk chocolates",cadbury2,"dark chocolates, and",cadbury3,"white chocolates")
cadburyBox (6,5,8)    


#example 3; longest way creating variables for amount of chocolate and name of chocolate
cadbury1 = "Milk Chocolate"
cadbury2 = "Dark Chocolate" #here we are making variables for the chocolate types
cadbury3 = "White Chocolate"

def cadburyBox(m,d,w): # now we are making a function to allow people to adjust the number of choclates
    print ("There are",m,cadbury1,d,cadbury2,",and",w,cadbury3) #we print the amt and type and substitue in both types of variables
cadburyBox (6,5,8) #now we plug in the amt of each type of chocolate

#using DICT to make code concise
choc1 = {"cadburymilk":6}
choc2 = {"cadburydark":5}
choc3 = {"cadburywhite":8}
print(choc1,choc2,choc3)

#eveneven more concise
chocolatebox = {"dark":5,"milk":6,"white":8}

#one line code practice; a list within a list
studentlist = [["steve",32,"M"], ["lia",28,"F"], ["vin", 45, "M"], ["katie",38,"f"]]

#run the code below to get the list above to appear as a list in the console
import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist, columns =("name","age","gender"))

studentdf

#chocolates in list form
chocolatelist = [["milk",6], ["dark",5], ["white",8]]
chocodf = pandas.DataFrame(chocolatelist, columns =("type","quantity"))
print(chocodf)

#students in list form and graphing
studentlist = [["steve",32,"M"], ["lia",28,"F"], ["vin", 45, "M"], ["katie",38,"f"]]
studentlist


studentdf = pandas.DataFrame(studentlist, columns =("name","age","gender"))
studentdf

studentdf2 = pandas.DataFrame(studentlist, columns =("name","age","gender"), index = ["1","2","3","4"])
studentdf2 

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go
studentbar = go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

#graphing chocolate bar
titles = go.Layout (title = "number of chocolates by type")
chocolatebar = go.Bar(x=chocodf["type"],y=chocodf["quantity"])
fig = go.Figure(data= [chocolatebar], layout=titles)
plot(fig)


