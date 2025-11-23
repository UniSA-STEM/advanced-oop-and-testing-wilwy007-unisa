'''
File: staff.py
Description: This module defines the staff structure for the Zoo Management System,
modelling the people who care for and manage the animals. At the core is the abstract
base class `Staff`, which represents a generic staff member and enforces that all subclasses
implement a `perform_duty` method. Two concrete subclasses, `Zookeeper` and `Veterinarian`,
inherit from `Staff` and implement role-specific responsibilities. Zookeepers are responsible
for feeding animals and maintaining clean enclosures, while veterinarians focus on conducting health
checks and managing animal welfare. By using abstraction, inheritance, and polymorphism, this module
allows the system to manage different types of staff in a flexible way, supporting both
current zoo operations and potential future staff roles.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import date
from animal import Animal

class Staff(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def perform_duty(self):
        pass


class Zookeeper(Staff):
    def perform_duty(self):
        return f"{self._name} is feeding animals and cleaning enclosures."

    def feed_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise TypeError("Can only feed an Animal instance.")
        return animal.eat()

    def clean_enclosure(self, enclosure):
        enclosure.clean()
        return f"{self._name} cleaned the enclosure '{enclosure._name}'."


class Veterinarian(Staff):
    def perform_duty(self):
        return f"{self._name} is performing health checks."

    def perform_health_check(self, animal: Animal, description: str, severity: str = "low"):
        if not isinstance(animal, Animal):
            raise TypeError("Health checks can only be performed on an Animal.")
        animal.add_health_record(description, severity)
        return f"{self._name} performed a health check on {animal._name}."

    def treat_animal(self, animal: Animal, description: str = "Treatment completed"):
        # Resolve all active health records
        for record in animal.get_health_records():
            if record["status"] == "active":
                record["status"] = "resolved"
                record["description"] += f" | {description}"
        return f"{self._name} treated {animal._name}."
