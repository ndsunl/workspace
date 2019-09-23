"""
类和对象的加强练习
"""


class CommonZombie:

    def __init__(self):
        self.healthPoint = 30
        self.damagePoint = 5

    def getHealthPoint(self):
        if self.healthPoint > 0:
            return self.healthPoint
        else:
            return "已经挂了！"

    def getDamagePoint(self):
        return self.damagePoint

    def beHit(self, lostPoint):
        self.healthPoint -= lostPoint
        return self.lostPoint


class PeaShooter:

    def __init__(self):
        self.healthPoint = 60
        self.damagePoint = 5

    def getHealthPoint(self):
        if self.healthPoint > 0:
            return self.healthPoint
        else:
            return "已经挂了"

    def getDamagePoint(self):
        return self.damagePoint


z1 = CommonZombie()
z2 = CommonZombie()
p1 = PeaShooter()

print("==当前状态==")
print(f"僵尸z1 HP: {z1.getHealthPoint()}")
print(f"僵尸z2 HP: {z2.getHealthPoint()}")
print(f"豌豆射手p1 HP: {p1.getHealthPoint()}")

print("==普通僵尸z1、z2进入花园==")

print(f"z1早")
