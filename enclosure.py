'''
File: enclosure.py
Description: This module defines the Enclosure class for the Zoo Management System, representing
the physical spaces where animals are housed. Each enclosure has the properties name,
size, environmental type, cleanliness level, and a restriction on the type of animal it can
contain. The class allows adding and removing animals while enforcing type
compatibility, cleaning the enclosure, and reporting its current status including the animals
it contains. The module ensures that enclosures are managed consistently, supports animal welfare,
and allows the system to maintain a clear overview of the zoo’s layout and operational conditions.
This design also supports future extensions, such as scheduling cleaning or feeding routines and
monitoring environmental factors.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name: str, size: int, environment_type: str, allowed_animal_type: type):
        if size <= 0:
            raise ValueError("Enclosure size must be positive.")
        if not environment_type:
            raise ValueError("Environment type must be provided.")

        self._name = name
        self._size = size
        self._environment_type = environment_type.lower()
        self._allowed_animal_type = allowed_animal_type
        self._animals = []
        self._cleanliness = 100

    def add_animal(self, animal):
        if not isinstance(animal, self._allowed_animal_type):
            raise TypeError(f"This enclosure only accepts {self._allowed_animal_type.__name__}.")

        if animal._environment != self._environment_type:
            raise ValueError(
                f"{animal._name} the {animal._species} requires a '{animal._environment}' "
                f"environment, but this enclosure is '{self._environment_type}'."
            )
        if animal in self._animals:
            raise ValueError(f"{animal._name} the {animal._species} is already in this enclosure.")

        self._animals.append(animal)
        animal.assign_enclosure(self)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            animal.assign_enclosure(None)

    def clean(self):
        self._cleanliness = 100

    def get_status(self):
        return {
            "name": self._name,
            "environment": self._environment_type,
            "cleanliness": self._cleanliness,
            "animals": [a._name for a in self._animals]
        }
