from encodings.punycode import selective_find
from random import randint

class cat:
    def  __init__(self, name):
        self.name = name
        self.gladness = 50
        self.playing = 0
        self.alive = True

    def to_play(self):
        print("time to play")
        self.playing += 0.12
        self.gladness += 3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.playing -= 0.07

    def to_eat(self):
        print("time to eat")
        self.gladness += 7
        self.playing -= 0.03

    def is_alaive(self):
        if self.playing < -0.5:
            print("time playing")
            self.alive = False

        elif self.gladness <= 0:
            print("Depresion")
            self.alive = False

        elif self.playing > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"playing = {round(self.playing, 2)}")

    def live(self,day):
        text_day = f"Day {day} of {self.name} live"
        print(f"{text_day:=^30}")
        cube = randint(1,4)
        if cube == 1:
            self.to_sleep()

        elif cube == 2:
            self.to_play()

        elif cube == 3:
            self.to_eat()

        else:
            self.to_chill()
        self.end_of_day()
        self.is_alaive()


nick = cat(name="Nick")
for day in range(365):
   if nick.alive == False:
       break
   nick.live(day)