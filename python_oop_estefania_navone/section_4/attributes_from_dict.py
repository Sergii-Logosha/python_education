person_info = {"name": "Irusia", "age": 35, "city": "New York"}


class Person:

    def __init__(self, info):
        for key, value in info.items():
            setattr(self, key, value)


irusya = Person(person_info)
print(irusya.name)
