# Dependency inversion principle states that entities must depend on abstractions and not on concretions. It states high level modules 
#  must not depend on low level module but they should depend on abstractions

# In other words, classes should depend on interfaces or abstract classes, not on concrete implementations.

# DIP violation - In this computer class is directly dependent on concrete class keyboard which violates the DIP

# class Keyboard :
#     def input(self):
#         return "Input from keyboard"
    
# class Computer:
#     def __init__(self):
#         self.keyboard = Keyboard()

#     def getInput(self):
#         return self.keyboard.input()
    

# computer = Computer()
# print(computer.getInput())

# DIP Fixed

from abc import ABC, abstractmethod

class InputDevice(ABC):
    @abstractmethod
    def input(self):
        pass

class Keyboard(InputDevice):
    def input(self):
        return "Input from keyboard"
    
class Touchpad(InputDevice):
    def input(self):
        return "Input from touchpad"
    
class Computer:
    def __init__(self, inputdevice: InputDevice):
        self.inputdevice = inputdevice

    def getInput(self):
        return self.inputdevice.input()
    
keyboard = Keyboard()
computer = Computer(keyboard)
print(computer.getInput())

touchpad = Touchpad()
comp = Computer(touchpad)
print(comp.getInput())


