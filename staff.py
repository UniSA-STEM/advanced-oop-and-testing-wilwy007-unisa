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

class Staff(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def perform_duty(self):
        pass


class Zookeeper(Staff):
    def perform_duty(self):
        return f"{self._name} is feeding animals and cleaning enclosures."


class Veterinarian(Staff):
    def perform_duty(self):
        return f"{self._name} is performing health checks."
