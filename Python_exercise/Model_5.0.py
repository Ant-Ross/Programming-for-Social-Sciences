# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:59:49 2018

@author: ts16larp
"""

import random
import operator
import matplotlib.pyplot
import numpy as np
import agentframework
import csv

# creating a distance function

def distance_between(a,b):
    return ((a.y - b.y)**2 + ((a.x - b.x)**2))**0.5
    

# creating an agent though a Class
a = agentframework.Agent()


# Parameters
agents = []
num_of_agents = 10
num_of_iterations = 200

# creating agents in a container

for i in range(num_of_agents):
    agents.append(agentframework.Agent())
    
# moving each agent n times. The moving code was modifyied so the agents can't get out of our 100 x 100 grid
       
for j in range(num_of_agents):      
    for i in range(num_of_iterations): 
        agents[j].move()
        
                    
# Plotting agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   
matplotlib.pyplot.show()


# Reading environment
f = open('env.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				# A list of rows
    rowlist = []	
    for value in row:				# A list of value
        rowlist.append(value)
        print(value) 				# Floats   
    environment.append(rowlist)  
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

import matplotlib.pyplot
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#Distance between all of the agents. Adding timing distance combinations

#start = time.clock()
#for j in range(num_of_agents):
#    for i in range(num_of_agents):
#        distance_between(i,j)
#end = time.clock()
#
#print("time = " + str(end - start))    