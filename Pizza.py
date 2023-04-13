# Name: Anushka Purwar
# Roll no.: E22MCAG0036
from abc import ABC,abstractmethod
class Pizza(ABC):
    def __init__(self, basePrice):
        self.__basePrice = basePrice
    
    def get_pizza_price(self):
        return self.__basePrice

    def calculateCost(self):
       pass
    
    def displayDetails(self):
       pass


