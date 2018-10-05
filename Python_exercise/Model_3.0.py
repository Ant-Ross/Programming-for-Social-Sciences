# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:20:24 2018

@author: ts16larp
"""

import random
import operator
import matplotlib.pyplot
import numpy as np
import time

# creating a distance function

def distance_between(a,b):
    distance = (((agents[a][0] - agents[b][0])**2) + ((agents[a][1] - agents[b][1])**2))**0.5
    print(distance)
    

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
                        

a = np.array(agents)

further_east = max(agents, key=operator.itemgetter(1))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])   
matplotlib.pyplot.scatter(further_east[1],further_east[0], color='red')
matplotlib.pyplot.show()

#Distance between all of the agents. Adding timing distance combinations

start = time.clock()
for j in range(num_of_agents):
    for i in range(num_of_agents):
        distance_between(i,j)
end = time.clock()

print("time = " + str(end - start))    
    
    

# distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
# print(distance)

