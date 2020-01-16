# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item = []
    # def __repr__(self):
    #     return self.name + '\n' + self.description
    def __str__(self):
        return f'{self.name}\n{self.description}\n Room Items: {self.item}'