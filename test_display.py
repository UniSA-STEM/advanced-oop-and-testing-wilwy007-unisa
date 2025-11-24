import pytest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from zoo import Zoo

# ANIMAL DISPLAY TESTS

def test_animal_display_details():
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    # initially no enclosure
    details = lion.display_details()
    print("\nAnimal Display Details:\n", details)
    assert "Leo" in details
    assert "Savannah" not in details.lower()  # no enclosure yet

    enc = Enclosure("Savannah", 100, "savannah", Mammal)
    enc.add_animal(lion)
    details_with_enc = lion.display_details()
    print("\nAnimal Display with Enclosure:\n", details_with_enc)
    assert "Savannah" in details_with_enc

def test_bird_reptile_display():
    penguin = Bird("Percy", "Penguin", 2, "fish", "arctic")
    snake = Reptile("Sly", "Snake", 4, "rats", "desert")
    print("\nBird Display:\n", penguin.display_details())
    print("\nReptile Display:\n", snake.display_details())
    assert "Percy" in penguin.display_details()
    assert "Sly" in snake.display_details()

# ENCLOSURE DISPLAY TESTS

def test_enclosure_display():
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    elephant = Mammal("Ella", "Elephant", 10, "plants", "savannah")
    enc = Enclosure("Savannah", 500, "savannah", Mammal)
    enc.add_animal(lion)
    enc.add_animal(elephant)

    details = enc.display_details()
    print("\nEnclosure Display Details:\n", details)
    assert "Savannah" in details
    assert "Leo" in details
    assert "Ella" in details

# STAFF DISPLAY TESTS

def test_staff_display_assignments():
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    enc = Enclosure("Savannah", 500, "savannah", Mammal)
    enc.add_animal(lion)

    keeper = Zookeeper("Sam")
    keeper.assign_enclosure(enc)
    vet = Veterinarian("Dr. Alice")
    vet.assign_animal(lion)

    print("\nZookeeper Display:\n", keeper.display_assignments())
    print("\nVeterinarian Display:\n", vet.display_assignments())
    assert "Sam" in keeper.display_assignments()
    assert "Dr. Alice" in vet.display_assignments()

# ZOO DISPLAY TEST

def test_zoo_display_status():
    zoo = Zoo()
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    penguin = Bird("Percy", "Penguin", 2, "fish", "arctic")

    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    bird_enc = Enclosure("Aviary", 200, "arctic", Bird)

    mammal_enc.add_animal(lion)
    bird_enc.add_animal(penguin)

    zoo.add_enclosure(mammal_enc)
    zoo.add_enclosure(bird_enc)

    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr. Alice")

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    zoo.assign_staff_to_enclosure(keeper, mammal_enc)
    zoo.assign_staff_to_animal(vet, lion)

    status = zoo.display_status()
    print("\nZoo Display Status:\n", status)
    assert "Savannah" in status
    assert "Aviary" in status
    assert "Leo" in status
    assert "Percy" in status
    assert "Sam" in status
    assert "Dr. Alice" in status