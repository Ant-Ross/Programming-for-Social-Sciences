# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random
import operator
import matplotlib.pyplot

#First set of variables
y0 = 50
x0 = 50

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)


#Second set of variables
y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

#Distance between points
distance = (((y1-y0)**2) + ((x1-x0)**2))**0.5

print(x0, y0, x1, y1, distance)


# CONTAINERS LESSON

#Generating random numbers with a specified range

y0 = random.randint(0,99)
x0 = random.randint(0,99)

agents = []
agents.append([y0,x0]) 

# function appends adds the element at the bottom of the list
#so you don't have to keep a record of the position every time you add a new element

# Getting rid of creating the coordinates at the begining
# Note that if you run this command over and over you just keep adding agents to the list (without emptying the list)
agents.append([random.randint(0,99),random.randint(0,99)])


# function max gives you the maximum value in a list taking into account the first element. The extra argument allows you to select
# the position of the element you want the max of 
print(max(agents, key=operator.itemgetter(1)))

# colouring the further east point, i.e. the one with the largest x coordinate.
# remember coordinates for our agents are in the form (y,x)

# creating a variable that contains a subset of the furthest east point
further_east = max(agents, key=operator.itemgetter(1))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(further_east[1],further_east[0], color='red')
matplotlib.pyplot.show()


# Loops

num_of_agents = 10

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

         
for j in range(len(agents)):  
    for i in range(2):    
        if random.random() < 0.5:
            agents[j][0] += 1
        else:
            agents[j][0] -= 1
        
        if random.random() < 0.5:
            agents[j][1] += 1
        else:
            agents[j][1] -= 1
    

        
    
    
    