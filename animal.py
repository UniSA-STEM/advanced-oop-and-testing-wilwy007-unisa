'''
File: animal.py
Description: This module defines the animal hierarchy for the Zoo Management System,
providing a structured way to represent the different animals in the zoo. At the core
is the abstract base class `Animal`, which defines common attributes such as name, species, age,
dietary needs, health records, and the enclosure to which the animal is assigned.
It also provides shared behaviors like eating, sleeping, and managing health records.
Specific types of animals are represented as subclasses—such as `Mammal`, `Bird`, and `Reptile`—which
inherit from `Animal` and implement their own unique behaviors, such as making species-specific sounds.
By using abstraction, inheritance, and polymorphism, this module allows the system to manage a variety of
animals consistently while supporting both shared and specialized behaviors, ensuring flexibility for future
animal types and zoo operations.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        if not name:
            raise ValueError("Animal name cannot be empty.")
        if not species:
            raise ValueError("Species cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not dietary_needs:
            raise ValueError("Dietary needs must be provided.")

        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs
        self._health_records = []
        self._enclosure = None

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return f"{self._name} the {self._species} is eating {self._dietary_needs}."

    def sleep(self):
        return f"{self._name} the {self._species} is sleeping."

    def add_health_record(self, record):
        self._health_records.append(record)

    def get_health_records(self):
        return self._health_records

    def assign_enclosure(self, enclosure):
        self._enclosure = enclosure

    def get_enclosure(self):
        return self._enclosure

class Mammal(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} makes a mammal sound."

class Bird(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} chirps."

class Reptile(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} hisses."
