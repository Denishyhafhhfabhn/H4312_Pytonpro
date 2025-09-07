from encodings.punycode import selective_find
from random import randint

class Student:
    def  __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.07

    def to_doplesson(self):
        print("Dop lesson")
        self.gladness -= 7
        self.progress += 0.3

    def is_alaive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False

        elif self.gladness <= 0:
            print("Depresion")
            self.alive = False

        elif self.progress > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"progress = {round(self.progress, 2)}")

    def live(self,day):
        text_day = f"Day {day} of {self.name} live"
        print(f"{text_day:=^30}")
        cube = randint(1,4)
        if cube == 1:
            self.to_sleep()

        elif cube == 2:
            self.to_study()

        elif cube == 3:
            self.to_doplesson()

        else:
            self.to_chill()
        self.end_of_day()
        self.is_alaive()


nick = Student(name="Nick")
for day in range(365):
   if nick.alive == False:
       break
   nick.live(day)