from encodings.punycode import selective_find
from random import randint

class Student:
    def  __init__(self, cat):
        self.cat = cat
        self.gladness = 50
        self.play = 0
        self.eat = 10
        self.alive = True

    def to_play(self):
        print("time to study")
        self.play += 0.12
        self.gladness -= 3
        self.eat -= 0.1

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3
        self.play -= 0.05
        self.eat -= 0.1

    def to_eat(self):
        print("eat")
        self.gladness += 5
        self.play -= 0.03
        self.eat += 0.5

    def to_progulka(self):
        print("progulka")
        self.gladness += 7
        self.play += 0.3

    def is_alaive(self):
        if self.play < -0.5:
            print("Cast out")
            self.alive = False

        elif self.gladness <= 0:
            print("Depresion")
            self.alive = False

        elif self.play > 5:
            print("Passed externally")
            self.alive = False

        elif self.eat <= 0:
            print("golod")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"play = {round(self.play, 2)}")

    def live(self,day):
        text_day = f"Day {day} of {self.cat} live"
        print(f"{text_day:=^40}")
        cube = randint(1,4)
        if cube == 1:
            self.to_sleep()

        elif cube == 2:
            self.to_eat()
            self.to_play()

        elif cube == 3:
            self.to_eat()
            self.to_progulka()

        else:

            self.to_eat()
        self.end_of_day()
        self.is_alaive()


nick = Student(cat="Nick")
for day in range(365):
   if nick.alive == False:
       break
   nick.live(day)