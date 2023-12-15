
from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculateSalary(self):
        pass
class Contractor(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculateSalary(self):
        return self.hours*self.rate

class FullTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
    def calculateSalary(self):
        return 1.2*self.hours*self.rate
akash = FullTimeEmployee(40,100)
nishant = Contractor(40,100)
print(f"Nishant's salary: {nishant.calculateSalary()}" )
print(f"Akash's salary: {akash.calculateSalary()}" )