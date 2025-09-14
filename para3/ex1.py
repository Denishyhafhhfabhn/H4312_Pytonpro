class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengere = []

    def add_passengere(self, human):
        self.passengere.append(human)

    def print_passenger(self):
        if self.passengere != []:
            print(f"names {self.brand} passenger")
            for person in self.passengere:
                print(person. name)

        else:
            print(f"names {self.brand} are no passenger")



person1 = Human("Nick")
person2 = Human("Lisa")
person3 = Human("Vasya")

avto = Auto("Mercedes")
avto.add_passengere(person1)
avto.add_passengere(person2)
avto.print_passenger()
avto.add_passengere(person3)
avto.print_passenger()
