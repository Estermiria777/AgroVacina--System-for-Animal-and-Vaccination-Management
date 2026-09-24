from class_animals import *

animal1 = Equine(1, "Formosa", "Mangalarga Marchador", 2)

animal2 = Bovine(2, "Mimosa", "Nelore", 4)

animal3 = Equine(3, "Estrela", "Puro Sangue Lusitano", 5)

print(animal1)
print("------------------")
animal1.mandatory_vaccines()
animal1.recommended_vaccines()
print("----------------------")
print(animal2)
print("------------------")
animal2.mandatory_vaccines()
animal2.recommended_vaccines()
print("-----------------------")
print(animal3)
animal3.mandatory_vaccines()
animal3.recommended_vaccines()




