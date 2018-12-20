class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


albert = Person("Albert", 18)
mary = Person("Mary", 20)
john = Person("John", 40)
cathy = Person("Cathy", 10)

people = [albert, mary, john, cathy]
print("sort by age")
for person in sorted(people, cmp=lambda a, b: 1 if a.age > b.age else -1 if a.age < b.age else 0):
    print(person.name)
print("sort by name")
for person in sorted(people, cmp=lambda a, b: 1 if a.name > b.name else -1 if a.name < b.name else 0):
    print(person.name)
