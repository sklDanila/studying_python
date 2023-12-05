class Person:
    type = "Person"

    def __init__(self, name):
        self.name = name


tom = Person("Tom")
bob = Person("Bob")
print(tom.type)  # Person
print(bob.type)  # Person

# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)  # Class Person
print(bob.type)  # Class Person
