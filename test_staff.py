import pytest
from staff import Staff, Zookeeper, Veterinarian
from animal import Mammal
from enclosure import Enclosure
from zoo import Zoo


# -----------------------------
# ZOOKEEPER TESTS
# -----------------------------
def test_zookeeper_feeds_and_cleans():
    zoo = Zoo()
    enc = Enclosure("Savannah", 100, "savannah", Mammal)
    zoo.add_enclosure(enc)
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    zoo.add_animal(lion, enc)

    keeper = Zookeeper("Sam")
    zoo.add_staff(keeper)
    zoo.assign_staff_to_enclosure(keeper, enc)

    result = keeper.perform_duty()

    print(f"Zookeeper duty output: {result}")
    print(f"Lion eats: {lion.eat()}")
    print(f"Enclosure cleanliness: {enc._cleanliness}")

    assert lion.eat() == "Leo the Lion is eating meat."
    assert enc._cleanliness == 100
    assert result == "Sam fed animals and cleaned assigned enclosures."


def test_zookeeper_no_duplicate_enclosure():
    enc = Enclosure("Savannah", 100, "savannah", Mammal)
    keeper = Zookeeper("Sam")
    keeper.assign_enclosure(enc)
    keeper.assign_enclosure(enc)
    print(f"Assigned enclosures (no duplicates): {keeper._assigned_enclosures}")
    assert keeper._assigned_enclosures.count(enc) == 1


# -----------------------------
# VETERINARIAN TESTS
# -----------------------------
def test_veterinarian_health_checks():
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    vet = Veterinarian("Dr. Alice")
    vet.assign_animal(lion)

    result = vet.perform_duty()

    print(f"Veterinarian duty output: {result}")
    print(f"Lion health status: {lion.get_health_status()}")

    assert lion.get_health_status() == "Healthy"
    assert result == "Dr. Alice performed health checks on assigned animals."


def test_veterinarian_no_duplicate_animal():
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    vet = Veterinarian("Dr. Alice")
    vet.assign_animal(lion)
    vet.assign_animal(lion)
    print(f"Assigned animals (no duplicates): {vet._assigned_animals}")
    assert vet._assigned_animals.count(lion) == 1


# -----------------------------
# ABSTRACT STAFF TEST
# -----------------------------
def test_cannot_instantiate_staff():
    with pytest.raises(TypeError) as e:
        Staff("Abstract")
    print(f"Attempted abstract Staff instantiation: {e.value}")


# -----------------------------
# ZOO DAILY ROUTINE TESTS
# -----------------------------
def test_zoo_daily_routine_updates():
    zoo = Zoo()
    enc = Enclosure("Savannah", 100, "savannah", Mammal)
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    zoo.add_enclosure(enc)
    zoo.add_animal(lion, enc)

    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr. Alice")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)
    zoo.assign_staff_to_enclosure(keeper, enc)
    zoo.assign_staff_to_animal(vet, lion)

    zoo.daily_routine()

    print(f"Enclosure cleanliness after daily routine: {enc._cleanliness}")
    print(f"Lion health status after daily routine: {lion.get_health_status()}")

    assert enc._cleanliness == 100
    assert lion.get_health_status() == "Healthy"


# -----------------------------
# ZOO ASSIGNMENT ERRORS
# -----------------------------
def test_assign_invalid_staff_type():
    zoo = Zoo()
    enc = Enclosure("Savannah", 100, "savannah", Mammal)

    class DummyStaff:
        pass

    dummy = DummyStaff()
    with pytest.raises(TypeError):
        zoo.assign_staff_to_enclosure(dummy, enc)


