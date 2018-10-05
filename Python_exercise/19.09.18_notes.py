# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:32:14 2018

@author: ts16larp
"""

# Creating a person using classes
class Person:
    def __init__(self, money, happiness):
        self.money = money
        self.happiness = happiness
        
    def work(self):
        """working increases money but decreases happiness"""
        self.money = self.money + 10
        self.happiness = self.happiness - 5

    def consume(self):
        """Consumption decreases money, increases happiness"""
        self.happiness += 7
        self.money -= 8
    
    def __repr__(self):
        return (f"A person with money = {self.money} "
                f"and happiness = {self.happiness}")

    def interact(self, other):
        """Interact with another person; increases happiness
        for both"""
        self.happiness += 1
        other.happiness += 1
        

jitse = Person(100, 10)        
jitse.work()
jitse.consume()
print("Jitse's money:", jitse.money)
print(f"Jitse: money = {jitse.money}, "
      f"happiness = {jitse.happiness}")

print(jitse)

rob = Person(500,5)
rob.interact(jitse)
print(jitse)
print (rob)


# Input and Output

# Reading a creating and reading a text file

my_file = open('hi.txt', 'w')
my_file.write('Oh hello!')
my_file.close()

file_for_reading = open('hi.txt', 'r')
text_in_file = file_for_reading.read()
file_for_reading.close() # remember to close the files cause it can carry problems further
print(text_in_file)


# Attempt 1: Reading everything
file_for_reading = open('agent-data.txt', 'r')
text_in_file = file_for_reading.read()
file_for_reading.close()

# Attempt 2: Use with so that you don't have to close
with open('agent-data.txt', 'r') as file_for_reading:
    text_in_file = file_for_reading.read()

# Attempt 3: Read line by line
with open('agent-data.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        print('I read a line and it is:', repr(line))

#Attempt 4: Split the words
with open('agent-data.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        print('I read a line and it is:', repr(line))
        
# Attempt 5: Construct people
with open('agent-data.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        money = int(words[0])
        happiness = int(words[1])
        person = Person(money, happiness)
        print('I read a line and it is:', repr(line))        


def read_persons_from_file(filename):
    """Return a list of Person. File should be a text file 
    with two numbers separated by space on each line"""
    persons = []
    with open(filename, 'r') as file_for_reading:
        for line in file_for_reading:
            words = line.split()
            money = int(words[0])
            happiness = int(words[1])
            person = Person(money, happiness)
            person.append(person)
        return persons

person_list = read_persons_from_file('agent-data.txt')
for person in person_list:
    person.work()
    
# numpym: numpy.loadtxt reads files and puts them in an array


import csv




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


import csv
f = open('env.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    for value in row:				# A list of value
        print(value) 				# Floats
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.










