from extras.scripts import *
from .models import Animal

name = "Animal-related scripts"

class AnimalScript(Script):
    class Meta:
        description = "What does the animal say?"

    animal = StringVar()

    def run(self, data, commit):
        try:
            animal = Animal.objects.get(name=data['animal'])
            self.log_success(f'The {animal.name} says "{animal.sound}"!')
        except Animal.DoesNotExist:
            self.log_failure(f'No such animal "{data["animal"]}"')

scripts = [AnimalScript]
