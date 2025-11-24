'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    lion = Mammal("Leo", 5, "meat")
    penguin = Bird("Pingu", 2, "fish")

    mammal_enclosure = Enclosure("Savannah Habitat", 500, "savannah", Mammal)
    bird_enclosure = Enclosure("Penguin Pool", 200, "aquatic", Bird)

    mammal_enclosure.add_animal(lion)
    bird_enclosure.add_animal(penguin)

    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr. Alice")

    print(lion.make_sound())
    print(penguin.eat())
    print(keeper.perform_duty())
    print(vet.perform_duty())

    print(mammal_enclosure.get_status())
    print(bird_enclosure.get_status())


if __name__ == "__main__":
    main()
