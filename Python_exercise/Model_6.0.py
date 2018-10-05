# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:19:31 2018

@author: ts16larp
"""
import random
import matplotlib.pyplot
import agentframework
import csv

# Reading environment
f = open('env.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				# A list of rows
    rowlist = []	
    for value in row:				# A list of value
        rowlist.append(value)
        #print(value) 				# Floats   
    environment.append(rowlist)  
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

    
# Parameters
agents = []
num_of_agents = 25
num_of_iterations = 15
neighbourhood = 20


# creating agents in a container
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))
       
    
# moving each agent n times. The moving code was modifyied so the agents can't get out of our 100 x 100 grid

       
for j in range(num_of_agents):
    random.shuffle(agents) # Shuffles the list in every new iteration   
    for i in range(num_of_iterations): 
        agents[j].move()
        agents[j].eat()
        agents[j].share_with_neighbours(neighbourhood)
        
                    
# Plotting agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment) 
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for i in range(num_of_agents):
    print(agents[i].store)

# Animation   
    



#Distance between all of the agents. Adding timing distance combinations

#start = time.clock()
#for j in range(num_of_agents):
#    for i in range(num_of_agents):
#        distance_between(i,j)
#end = time.clock()
#
#print("time = " + str(end - start))    