class Person:
    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


#  класс работника
class Employee(Person):
    def work(self):
        print(f"{self.name} works")


#  класс студента
class Student(Person):
    def study(self):
        print(f"{self.name} studies")


def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()


tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)  # Tom works
act(bob)  # Bob studies
act(sam)  # Sam does nothing
