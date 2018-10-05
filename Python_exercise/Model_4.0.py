# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:34:47 2018

@author: ts16larp
"""

import random
import operator
import matplotlib.pyplot
import numpy as np
import agentframework

# creating an agent through a Class
a = agentframework.Agent()

# creating a distance function

def distance_between(a,b):
    distance = (((agents[a][0] - agents[b][0])**2) + ((agents[a][1] - agents[b][1])**2))**0.5
    print(distance)
    
# Parameters
agents = []
num_of_agents = 10
num_of_iterations = 200

# creating agents in a container

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    
# moving each agent n times. The moving code was modifyied so the agents can't get out of our 100 x 100 grid
       
for j in range(len(agents)):  
    
    for i in range(num_of_iterations): 
        
        if random.random() < 0.5:
            agents[j][0] = (agents[j][0] + 1) % 100
        else:
            agents[j][0] = (agents[j][0] - 1) % 100
        
        if random.random() < 0.5:
            agents[j][1] = (agents[j][1] + 1) % 100
        else:
            agents[j][1] = (agents[j][1] - 1) % 100
                        


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])   
matplotlib.pyplot.show()

#Distance between all of the agents. Adding timing distance combinations

#start = time.clock()
#for j in range(num_of_agents):
#    for i in range(num_of_agents):
#        distance_between(i,j)
#end = time.clock()
#
#print("time = " + str(end - start))    