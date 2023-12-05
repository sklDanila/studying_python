class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return (
            f"Invalid value: {self.age}. "
            f"Age must be between {self.minage} to {self.maxage}"
        )


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Name: {self.__name}  Age: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info()  # Name: Tom  Age: 37

    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e)
