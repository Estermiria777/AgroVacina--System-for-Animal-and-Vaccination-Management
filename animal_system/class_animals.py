from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, id, name, greed, age):
        self.id = id
        self.name = name
        self.greed=greed
        self.age = age


    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Breed: {self.greed}\n"
            f"Age: {self.age}"
        )
        
    @abstractmethod
    def mandatory_vaccines(self):
        pass

    @abstractmethod
    def recommended_vaccines(self):
        pass


class Bovine(Animal):
    def __init__(self, id, name, greed, age):
        super().__init__(id, name, greed,age)

    def mandatory_vaccines(self):
        print(
            "Here is the list of mandatory vaccines for Bovines:\n"
            "- Brucellosis vaccine\n"
            "- Foot-and-Mouth Disease vaccine\n"
            "- Rabies vaccine"
        )

    def recommended_vaccines(self):
        print(
            "Here is the list of recommended vaccines for Bovines:\n"
            "- Clostridial vaccine\n"
            "- Leptospirosis vaccine\n"
            "- Bovine Viral Diarrhea vaccine\n"
            "- Campylobacteriosis vaccine"
        )

class Equine(Animal):
    def __init__(self, id, name, greed, age):
        super().__init__(id, name, greed, age)

    def mandatory_vaccines(self):
        print(
            "Here is the list of mandatory vaccines for Equines:\n"
            "- Influenza\n"
            "- Encephalomyelitis\n"
            "- Rabies\n"
        )

    def recommended_vaccines(self):
        print(
            "Here is the list of recommended vaccines for Equines:\n"
            "- Tetanus\n"
            "- Rhinopneumonitis\n"
            "- Strangles and Leptospirosis\n"

        )
