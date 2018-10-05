
# Jitse Niesen j.niesen@leeds.ac.uk

class Person:
    def __init__(self, money, happiness):
        self.money = money
        self.happiness = happiness
        
    def work(self):
        """Working increases money but decreases happiness"""
        self.money = self.money + 10
        self.happiness = self.happiness - 5
        # or: self.happiness -= 5
        
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
        print('I read a line and it is: ', repr(line))
        
# Attempt 4: Split the words
with open('agent-data.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        print('I read a line and it is: ', repr(words))

# Attempt 5: Construct persons
with open('agent-data.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        money = int(words[0])
        happiness = int(words[1])
        person = Person(money, happiness)
        print('I read a line and I created: ', person)
        
def read_persons_from_file(filename):
    """Return a list of Person. File should be a text file
    with two numbers separated by space on each line."""
    persons = []
    with open(filename, 'r') as file_for_reading:
        for line in file_for_reading:
            words = line.split()
            money = int(words[0])
            happiness = int(words[1])
            person = Person(money, happiness)
            persons.append(person)
    return persons

# Read data from file and let everybody work
person_list = read_persons_from_file('agent-data.txt')
for person in person_list:
    person.work()

def write_persons_to_file(filename, persons):
    """Save a list of Person to file so that it can be read
    by read_persons_from_file."""
    with open(filename, 'w') as file_for_writing:
        for person in persons:
            s = f'{person.money} {person.happiness}\n'
            file_for_writing.write(s)
            
write_persons_to_file('workieworkie.txt', person_list)
