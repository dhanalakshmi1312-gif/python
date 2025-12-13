from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob   

    def age(self):
        today = date.today()
        birth = date(self.dob[0], self.dob[1], self.dob[2])
        age = today.year - birth.year
        return age


p = Person("Divya", "India", (2005, 6, 15))
print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.age())
