# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:16:59 2018

@author: ts16larp
"""

import random
import operator
import matplotlib.pyplot

agents = []

agents.append([random.randint(0,99),random.randint(0,99)])

further_east = max(agents, key=operator.itemgetter(1))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(further_east[1],further_east[0], color='red')
matplotlib.pyplot.show()

num_of_agents = 10

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])