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
    approved_breeds = ["Pug", "Beagle", "Bulldog", "Poodle", "Labrador"]

    def __init__(self, name=None, breed=None):
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
            else:
                self.name = name

        if breed is not None:
            if not isinstance(breed, str) or breed not in Dog.approved_breeds:
                print("Breed must be in list of approved breeds.")
            else:
                self.breed = breed

