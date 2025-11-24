import pytest
from animal import Mammal, Bird, Reptile

#   CREATION TESTS

def test_mammal_creation():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    print(f"\nMammal created: Name={m._name}, Species={m._species}, Age={m._age}, "
          f"Diet={m._dietary_needs}, Environment={m._environment}")
    assert m._name == "Leo"
    assert m._species == "Lion"
    assert m._age == 5
    assert m._dietary_needs == "meat"
    assert m._environment == "savannah"

def test_bird_creation():
    b = Bird("Percy", "Penguin", 2, "fish", "arctic")
    print(f"\nBird created: Name={b._name}, Species={b._species}, Environment={b._environment}")
    assert b._species == "Penguin"
    assert b._environment == "arctic"

def test_reptile_creation():
    r = Reptile("Sly", "Snake", 3, "rats", "desert")
    print(f"\nReptile created: Name={r._name}, Species={r._species}, Environment={r._environment}")
    assert r._species == "Snake"
    assert r._environment == "desert"

#   SOUND TESTS

def test_mammal_sound():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    result = m.make_sound()
    print(f"\nMammal sound: {result}")
    assert result == "Leo the Lion makes a mammal sound."

def test_bird_sound():
    b = Bird("Percy", "Penguin", 2, "fish", "arctic")
    result = b.make_sound()
    print(f"\nBird sound: {result}")
    assert result == "Percy the Penguin chirps."

def test_reptile_sound():
    r = Reptile("Sly", "Snake", 3, "rats", "desert")
    result = r.make_sound()
    print(f"\nReptile sound: {result}")
    assert result == "Sly the Snake hisses."

#   EAT & SLEEP TESTS

def test_animal_eat():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    result = m.eat()
    print(f"\nEating: {result}")
    assert result == "Leo the Lion is eating meat."


def test_animal_sleep():
    b = Bird("Percy", "Penguin", 2, "fish", "arctic")
    result = b.sleep()
    print(f"\nSleeping: {result}")
    assert result == "Percy the Penguin is sleeping."

#   HEALTH RECORD TESTS

def test_add_health_record():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    m.add_health_record("Leg wound")
    m.add_health_record("Medication administered")
    records = m.get_health_records()
    print(f"\nHealth records: {records}")

    assert [r["description"] for r in records] == [
        "Leg wound",
        "Medication administered"
    ]
    assert all(r["status"] == "active" for r in records)
    assert all(r["severity"] == "low" for r in records)


def test_add_health_record_custom_values():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    m.add_health_record("Broken leg", status="urgent", severity="high")
    rec = m.get_health_records()[0]
    print(f"\nCustom health record: {rec}")
    assert rec["status"] == "urgent"
    assert rec["severity"] == "high"


def test_clear_health_records():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    m.add_health_record("Injury")
    m.add_health_record("Medication")
    print(f"\nBefore clearing, health records: {m.get_health_records()}")

    m.clear_health_records()
    print(f"After clearing, health records: {m.get_health_records()}")

    assert m.get_health_records() == []
    assert m.get_health_status() == "Healthy"

#   HEALTH STATUS TESTS

def test_default_health_status():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    print(f"\nDefault health status: {m.get_health_status()}")
    assert m.get_health_status() == "Healthy"

def test_health_status_update():
    b = Bird("Percy", "Penguin", 2, "fish", "arctic")
    b.add_health_record("Under Treatment – wing injury")
    print(f"\nUpdated health status: {b.get_health_status()}")
    assert b.get_health_status() == "Under Treatment"

def test_health_status_multiple_records():
    r = Reptile("Sly", "Snake", 4, "rats", "desert")
    r.add_health_record("Under Treatment – infection")
    r.add_health_record("Medication")
    print(f"\nMultiple records health status: {r.get_health_status()}")
    assert r.get_health_status() == "Under Treatment"

def test_health_status_all_resolved():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    m.add_health_record("Injury", status="resolved")
    m.add_health_record("Medication", status="resolved")
    print(f"\nAll resolved health status: {m.get_health_status()}")
    assert m.get_health_status() == "Healthy"

#   ENCLOSURE TESTS

def test_assign_enclosure():
    m = Mammal("Leo", "Lion", 5, "meat", "savannah")
    fake_enclosure = object()
    m.assign_enclosure(fake_enclosure)
    print(f"\nAssigned enclosure: {m.get_enclosure()}")
    assert m.get_enclosure() == fake_enclosure


def test_reassign_enclosure():
    b = Bird("Percy", "Penguin", 2, "fish", "arctic")
    e1 = object()
    e2 = object()
    b.assign_enclosure(e1)
    b.assign_enclosure(e2)
    print(f"\nReassigned enclosure: {b.get_enclosure()}")
    assert b.get_enclosure() == e2

#   VALIDATION TESTS

def test_invalid_name():
    with pytest.raises(ValueError):
        Mammal("", "Lion", 5, "meat", "savannah")


def test_invalid_species():
    with pytest.raises(ValueError):
        Mammal("Leo", "", 5, "meat", "savannah")


def test_negative_age():
    with pytest.raises(ValueError):
        Mammal("Leo", "Lion", -1, "meat", "savannah")


def test_empty_dietary_needs():
    with pytest.raises(ValueError):
        Mammal("Leo", "Lion", 5, "", "savannah")


def test_empty_environment():
    with pytest.raises(ValueError):
        Mammal("Leo", "Lion", 5, "meat", "")


def test_unusual_characters_in_name():
    m = Mammal("Mr. Fluffy #1", "Cat", 3, "fish", "house")
    print(f"\nUnusual name: {m._name}")
    assert m._name == "Mr. Fluffy #1"


def test_extreme_age():
    m = Mammal("Turtle Elder", "Tortoise", 150, "plants", "grasslands")
    print(f"\nExtreme age: {m._age}")
    assert m._age == 150


