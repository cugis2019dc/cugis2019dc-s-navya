# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:50:21 2019

@author: STEM
"""
#example one for adding chocolate
cadburyBOX = 5
def cadbury(a):
    cadbury  = a+10
    print (cadbury)
cadbury (5)

#example two for adding chocolate

def cadburybox(b,a):
    cadburybox = a+b
    print (cadburybox)
    
cadburybox(15,5)

#example for how to have word varaibles instead of numbers
def cadburyBox (m,d,w):
    print("There is",m,",",d,",",w,"in the box")
    
cadburyBox ("White Chocolate", "Dark Chocolate", "Milk Chocolate")


#greeting person by name
print ("hello navya")
# example 2
def hello(a):
    hello = a
    print("Hello", a)
 hello("navya")
 
 # example 3  
 a = "navya"print("hello", a)
 
 #ex 4
 name = input ("please enter your name") #this is similar to def line where you identify the variable (name)
 print ("your name is", name)
 
 age = input("please enter your age")
 print ("Thank you. You entered", age)
 
 #random stuff
 
 ageint = int(age)
 age int
 
 ageint = float(age)
 
 import math
 
 dir(math)
 
 math.pi
 math.factorial(12)
 
 math.pow(6,15)

#doing cubic root of x ex 1
x = 8
cubicroot = math.pow(x,1/3)
print ("The cubic root of",x,"is",cubicroot)

#doing cubic root of x ex 2
def cubic(x):
    cubic = math.pow(x,1/3)
    print ("The cubic root of",x,"is",cubic)
    
cubic(8)

#doing cubic root of a variable using input function (doesnt work)
a = int(input("please enter a value"))
def cubic(a):
    cubic = math.pow(a, 1/3)
    print ("The cubic root of",a,"is",cubic)
    
cubic(8)





 
 
 

 