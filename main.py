'''
File: main.py
Description: Demonstration script for the Zoo Management System.
Shows creation and management of animals, enclosures, and staff.
Demonstrates behaviors (sounds, eating, sleeping), staff duties
(feeding, cleaning, health checks), animal health management,
movement rules, and zoo status reporting.
Author: William Willoughby
ID: 110477792
Username: wilwy007
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from zoo import Zoo

print("\n=== Welcome to the Zoo Demonstration ===\n")


# Create Animals

leo = Mammal("Leo", "Lion", 5, "meat", "savannah")
ella = Mammal("Ella", "Elephant", 10, "plants", "savannah")
percy = Bird("Percy", "Penguin", 2, "fish", "arctic")
sly = Reptile("Sly", "Snake", 4, "rodents", "desert")

animals = [leo, ella, percy, sly]

print("--- Animals Created ---")
for a in animals:
    print(f"{a._name} the {a._species} | Age: {a._age} | Diet: {a._dietary_needs} | Env: {a._environment}")

# Animal behaviors

print("\n--- Animal Behaviors ---")
for a in animals:
    print(f"{a._name} makes sound: {a.make_sound()}")
    print(f"{a._name} eats: {a.eat()}")
    print(f"{a._name} sleeps: {a.sleep()}")


# Create Enclosures

savannah_enc = Enclosure("Savannah", 500, "savannah", Mammal)
new_savannah_enc = Enclosure("Savannah 2", 300, "savannah", Mammal)
aviary = Enclosure("Aviary", 200, "arctic", Bird)
reptile_house = Enclosure("Reptile House", 150, "desert", Reptile)

enclosures = [savannah_enc, new_savannah_enc, aviary, reptile_house]

print("\n--- Enclosures Created ---")
for enc in enclosures:
    print(f"{enc._name} | Size: {enc._size} | Env: {enc._environment_type} | Allowed: {enc._allowed_animal_type.__name__}")


# Initialise Zoo and Add Animals

zoo = Zoo()
for enc in enclosures:
    zoo.add_enclosure(enc)

zoo.add_animal(leo, savannah_enc)
zoo.add_animal(ella, savannah_enc)
zoo.add_animal(percy, aviary)
zoo.add_animal(sly, reptile_house)


# Staff Assignment

sam = Zookeeper("Sam")
dr_alice = Veterinarian("Dr. Alice")
zoo.add_staff(sam)
zoo.add_staff(dr_alice)

zoo.assign_staff_to_enclosure(sam, savannah_enc)
zoo.assign_staff_to_enclosure(sam, aviary)
zoo.assign_staff_to_enclosure(sam, reptile_house)

zoo.assign_staff_to_animal(dr_alice, leo)
zoo.assign_staff_to_animal(dr_alice, sly)


# Display Zoo Status

print("\n--- Initial Zoo Status ---")
print(zoo.display_status())


# Health Records Example

print("\n--- Health Record Example ---")
ella.add_health_record("Foot injury", status="active")
print(f"{ella._name} health status: {ella.get_health_status()}")


# Moving Animals Example

print("\n--- Moving Animals ---")

# Attempt to move under-treatment animal

try:
    zoo.remove_animal(ella)
    zoo.add_animal(ella, new_savannah_enc)
except ValueError as e:
    print(f"Error moving {ella._name}: {e}")

# Resolve Ella's health records

for rec in ella.get_health_records():
    rec['status'] = 'resolved'

# Now move her successfully

zoo.remove_animal(ella)
zoo.add_animal(ella, new_savannah_enc)
print(f"{ella._name} successfully moved to {ella.get_enclosure()._name}")

# Attempt to move Percy to wrong enclosure type

try:
    zoo.remove_animal(percy)
    zoo.add_animal(percy, savannah_enc)
except (ValueError, TypeError) as e:
    print(f"Error moving {percy._name}: {e}")


# Daily Routine with Display

print("\n--- Daily Routine ---")
for staff in zoo._staff:
    action_result = staff.perform_duty()
    print(action_result)  # shows feeding, cleaning, health checks

# Show updated enclosure cleanliness and health

print("\n--- Enclosure Cleanliness and Health Summary After Routine ---")
for enc in enclosures:
    print(f"{enc._name} cleanliness: {enc._cleanliness}")
    print(f"{enc._name} health summary: {enc.get_health_summary()}")


# List Animals by Species

print("\n--- Animals by Species ---")
species_dict = zoo.list_animals_by_species()
for species, names in species_dict.items():
    print(f"{species}: {names}")


# List Animals Under Treatment

print("\n--- Animals Under Treatment ---")
under_treatment = zoo.list_animals_under_treatment()
print(under_treatment if under_treatment else "None")


# Zoo Health Report

print("\n--- Zoo Health Report ---")
health_report = zoo.generate_health_report()
for name, status in health_report.items():
    print(f"{name}: {status}")


# Final Zoo Status

print("\n--- Final Zoo Status ---")
print(zoo.display_status())

print("\n=== End of Zoo Demonstration ===")
