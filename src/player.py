# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, location):
        self.location = location
        self.item = []
    def __repr__(self):
        return f'Your location is the: \n{self.location}\n'
    def __str__(self):
        return f'{self.item}'
