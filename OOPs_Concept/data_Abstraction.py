# Smaple

from abc import ABC,abstractmethod

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("Car Engine Started")
    def stop(self):
        print("Car Engine Stopped")

vehicle1 = car()
vehicle1.start()
vehicle1.stop()

# Real-time Program

from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

# Conrete Class
class SBI(ATM):
    def __init__(self,balance=0):
        self.__balance = balance # hidden data

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited amount. New Balance = {self.__balance}")

    def withdraw(self,amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
            print(f"Balance amount. New Balance = {self.__balance}")
        else:
            print("Insufficient Balance")

atm = SBI(5000)
atm.deposit(1000)
atm.withdraw(500)