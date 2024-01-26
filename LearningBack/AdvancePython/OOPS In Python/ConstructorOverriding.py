class Person:
    def __init__(self) -> None:
        print("Parent Class")

class Student(Person):
    def __init__(self) -> None:
        # super().__init__()
        print("Child Class constructor")

s1=Student()

