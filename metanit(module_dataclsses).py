from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")  # Name: Tom  Age: 38

"""
С помощью параметров декоратор dataclass позволяет сгенерировать дополнительный шаблонный код и вообще настроить генерацию кода:

def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False, match_args=True,
              kw_only=False, slots=False)
              
init: если равно True, то генерируется функция __init__(). По умолчанию равно True

repr: если равно True, то генерируется функция __repr__(), которая возвращает строковое представление объекта. По умолчанию равно True

eq: если равно True, то генерируется функция __eq__(), которая сравнивает два объекта. По умолчанию равно True

order: если равно True, то генерируются функции __lt__ (операция <), __le__ (<=), __gt__ (>), __ge__ (>=), которые применяются для упорядочивания объектов. По умолчанию равно False

unsafe_hash: если равно True, то генерируется функция __hash__(), которая возвращает хеш объекта. По умолчанию равно False

Применение параметров:         
"""

from dataclasses import dataclass


@dataclass(unsafe_hash=True, order=True)
class Person:
    name: str
    age: int

    def __repr__(self):
        return f"Person. Name: {self.name}  Age: {self.age}"


tom = Person("Tom", 38)
print(tom.__hash__())  # -421667297069596717
print(tom)  # Person. Name: Tom  Age: 38
