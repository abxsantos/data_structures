import pytest


class AnimalShelter(object):
    def __init__(self):
        self.all_animals = []
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if animal["animal"] == "cat":
            self.cats.append(animal)
            self.all_animals.append(animal)
        elif animal["animal"] == "dog":
            self.dogs.append(animal)
            self.all_animals.append(animal)
        else:
            return None

    def dequeue(self, cat=False, dog=False):
        if cat is True and dog is False:
            self.cats.pop(0) if self.cats else None
        elif dog is True and cat is False:
            self.dogs.pop(0) if self.dogs else None
        else:
            adopted_animal = self.all_animals.pop(0)
            self.cats.pop(0) if adopted_animal["animal"] == "cat" else self.dogs.pop(0)


@pytest.fixture(scope="function")
def animal_shelter():
    animal_shelter = AnimalShelter()
    return animal_shelter


@pytest.fixture(scope="function")
def animal_shelter_with_animals():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue({"animal": "cat"})
    animal_shelter.enqueue({"animal": "dog"})
    return animal_shelter


class TestAnimalShelter(object):
    def test_enqueue_a_cat(self, animal_shelter):
        animal_shelter.enqueue({"animal": "cat"})
        assert animal_shelter.cats == [{"animal": "cat"}]
        assert animal_shelter.dogs == []

    def test_enqueue_a_dog(self, animal_shelter):
        animal_shelter.enqueue({"animal": "dog"})
        assert animal_shelter.dogs == [{"animal": "dog"}]
        assert animal_shelter.cats == []

    def test_dequeue_any(self, animal_shelter_with_animals):
        animal_shelter_with_animals.dequeue()
        assert animal_shelter_with_animals.cats == []
        assert animal_shelter_with_animals.dogs == [{"animal": "dog"}]

    def test_dequeue_cat(self, animal_shelter_with_animals):
        animal_shelter_with_animals.dequeue(cat=True)
        assert animal_shelter_with_animals.cats == []
        assert animal_shelter_with_animals.dogs == [{"animal": "dog"}]

    def test_dequeue_dog(self, animal_shelter_with_animals):
        animal_shelter_with_animals.dequeue(dog=True)
        assert animal_shelter_with_animals.cats == [{"animal": "cat"}]
        assert animal_shelter_with_animals.dogs == []
