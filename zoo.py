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
        if isinstance(staff_member, Zookeeper):
            staff_member.assign_enclosure(enclosure)

    def assign_staff_to_animal(self, staff_member, animal):
        if isinstance(staff_member, Veterinarian):
            staff_member.assign_animal(animal)

    def generate_health_report(self):
        report = {}
        for enc in self._enclosures:
            report.update(enc.get_health_summary())
        return report

    def daily_routine(self):
        for staff in self._staff:
            staff.perform_duty()
