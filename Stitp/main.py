import _thread
import time
import random

maxSpeed = 10
numOfshijie = 10
mindis = 5
maxdis = 50
shijieG = []
desx = 0.0
desy = 0.0


class shijieQ:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.speedx = 0.0
        self.speedy = 0.0
        self.id = -1

    def init(self, tempx, tempy, tempid):
        self.y = tempy
        self.x = tempx
        self.id = tempid

    def update(self):
        self.x += self.speedx / 10
        self.y += self.speedy / 10
        temp = True
        while temp:
            temp = False
            self.speedx = maxSpeed * (random.randint(-100, 50) + (50 if desx > self.x else 0)) / 100
            self.speedy = maxSpeed * (random.randint(-100, 50) + (50 if desy > self.y else 0)) / 100
            if self.speedx * self.speedx + self.speedy * self.speedy > maxSpeed * maxSpeed:
                temp = True
                continue
            for index in range(numOfshijie):
                if index != self.id:
                    if None:
                        temp = True
        # print(self.id)


def upDates(index):
    while 1:
        shijieG[index].update()
        time.sleep(1)


def command():
    global desx
    global desy

    while 1:
        print("des x:")
        desx = float(input())
        print("des y:")
        desy = float(input())


def run():
    for i in range(numOfshijie):
        shijieG.append(shijieQ())
        shijieG[i].init(float(i) * 20, 0.0, int(i))
        print(shijieG[i].x, shijieG[i].y)

    for i in range(numOfshijie):
        try:
            _thread.start_new_thread(upDates, (i,))
        except (RuntimeError, KeyboardInterrupt):
            print("error " + i)

    try:
        _thread.start_new_thread(command, ())
    except (RuntimeError, KeyboardInterrupt):
        print("error command")

    while 1:
        pass


if __name__ == '__main__':
    run()
