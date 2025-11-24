'''
File: animal.py
Description: Defines the Animal base class and specific subclasses (Mammal, Bird, Reptile)
for the Zoo Management System. Implements core attributes and behaviors
(name, species, age, diet, environment) and supports health record management.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import date

class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str, environment: str):
        if not name:
            raise ValueError("Animal name cannot be empty.")
        if not species:
            raise ValueError("Species cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not dietary_needs:
            raise ValueError("Dietary needs must be provided.")
        if not environment:
            raise ValueError("Environment type must be provided.")

        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs
        self._environment = environment.lower()
        self._health_records = []
        self._enclosure = None

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return f"{self._name} the {self._species} is eating {self._dietary_needs}."

    def sleep(self):
        return f"{self._name} the {self._species} is sleeping."

    def add_health_record(self, description: str, severity: str = "low", status: str = "active", record_date: date = None):
        if not record_date:
            record_date = date.today()
        record = {
            "description": description,
            "date": record_date,
            "severity": severity.lower(),
            "status": status.lower()  # active, resolved
        }
        self._health_records.append(record)

    def get_health_records(self):
        return self._health_records

    def clear_health_records(self):
        self._health_records = []

    def is_healthy(self):
        return all(record.get("status") != "active" for record in self._health_records)

    def get_health_status(self):
        if not self._health_records:
            return "Healthy"
        for record in self._health_records:
            if record.get("status") == "active" or "under treatment" in record["description"].lower():
                return "Under Treatment"
        return "Healthy"

    def assign_enclosure(self, enclosure):
        self._enclosure = enclosure

    def get_enclosure(self):
        return self._enclosure

    def get_environment(self):
        return self._environment

    def display_details(self):
        return (
            f"Name: {self._name}\n"
            f"Species: {self._species}\n"
            f"Age: {self._age}\n"
            f"Dietary Needs: {self._dietary_needs}\n"
            f"Environment: {self._environment}\n"
            f"Health Status: {self.get_health_status()}\n"
            f"Enclosure: {self._enclosure._name if self._enclosure else 'None'}"
        )


class Mammal(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} makes a mammal sound."


class Bird(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} chirps."


class Reptile(Animal):
    def make_sound(self):
        return f"{self._name} the {self._species} hisses."
