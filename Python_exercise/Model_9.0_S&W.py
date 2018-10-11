# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:11:41 2018

@author: mcyitlr4
"""

import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework_v2
import csv
#import sys

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
wolves = []
num_of_agents = 15
num_of_wolves = 50
num_of_iterations = 10
neighbourhood = 20
scope = 10
# Plotting settings
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# creating sheeps and wolves
for i in range(num_of_agents):
    agents.append(agentframework_v2.Agent(environment, agents, neighbourhood))
    
for i in range(num_of_wolves):
    wolves.append(agentframework_v2.Wolf(agents, scope))    
    
    
       
#Movement, eating and sharing     
# Defining a function to be called in the animation commando further below
    
carry_on = True    
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    if len(agents) == 0: #it will check if every agent has eaten over n value 
        carry_on=False # when the above condition is met it will stop
        print("stopping condition")
       
    for j in range(len(agents)):
        random.shuffle(agents) # Shuffles the list in every new iteration   
        for i in range(num_of_iterations): 
            agents[j].move()
            agents[j].eat()
            agents[j].share_with_neighbours(neighbourhood)
            #print(agents[i].store)
            #print(len(agents))    
                  
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker="*", color='yellow') 
            
        
    for j in range(num_of_wolves):
        random.shuffle(wolves)
        for i in range(num_of_iterations):
            wolves[j].move()
            wolves[j].hunt(agents)                      
        
    for i in range(num_of_wolves):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color='black')   
    
        
    matplotlib.pyplot.ylim(0, 300) #modifyed so they use the whole image
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment) 
    
    
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (carry_on):
        yield a			# Returns control and waits next call.
        a = a + 1        
        #print(a)   

    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False,frames=num_of_iterations) 
                                              
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, frames=gen_function, repeat=False)
matplotlib.pyplot.show()
        
print(len(agents))                       

#for i in range(num_of_agents):
 #   print(agents[i].store)

