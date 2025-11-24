from staff import Zookeeper, Veterinarian

class Zoo:
    def __init__(self):
        self._enclosures = []
        self._staff = []
        self._animals = []

    def add_enclosure(self, enclosure):
        self._enclosures.append(enclosure)

    def add_staff(self, staff):
        self._staff.append(staff)

    def add_animal(self, animal, enclosure):
        enclosure.add_animal(animal)
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            enc = animal.get_enclosure()
            if enc:
                enc.remove_animal(animal)
            self._animals.remove(animal)

    def assign_staff_to_enclosure(self, staff_member, enclosure):
        from staff import Zookeeper  # ensure imported
        if not isinstance(staff_member, Zookeeper):
            raise TypeError(f"Only Zookeeper objects can be assigned to enclosures, got {type(staff_member)}")
        if enclosure not in staff_member._assigned_enclosures:
            staff_member.assign_enclosure(enclosure)

    def assign_staff_to_animal(self, staff_member, animal):
        from staff import Veterinarian
        if not isinstance(staff_member, Veterinarian):
            raise TypeError(f"Only Veterinarian objects can be assigned to animals, got {type(staff_member)}")
        if animal not in staff_member._assigned_animals:
            staff_member.assign_animal(animal)

    def generate_health_report(self):
        report = {}
        for enc in self._enclosures:
            report.update(enc.get_health_summary())
        return report

    def daily_routine(self):
        for staff in self._staff:
            staff.perform_duty()
