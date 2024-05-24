#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Unknown",breed="Unknown"):
     self.name=name
     self.breed=breed
    def name(self):
        return self._name
    
    def set_name(self,name):
        if isinstance(name,str) and 1<len(name)<25:
            self._name=name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name=None
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            print(breed)
            self.breed=breed

        else:
            print("The breed must be in the following list of dog breeds")
            print(", ".join(APPROVED_BREEDS))
            self._breed = None

