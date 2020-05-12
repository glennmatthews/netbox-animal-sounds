from extras.reports import *
from .models import Animal

name = "Animal-related reports"

class AnimalReport(Report):
    description = "Validate that every animal has a sound"

    def test_sound(self):
        for animal in Animal.objects.all():
            if animal.sound:
                self.log_success(animal, f"The {animal.name} says {animal.sound}")
            else:
                self.log_failure(animal, f"The {animal.name} makes no sound!")

reports = [AnimalReport]
