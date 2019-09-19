"""
普通僵尸类
"""

class CommonZombie:

    def __init__(self):
        self.healthPoint = 30           # 生命值 HP
        self.damagePoint = 5            # 伤害值 DP

    def showHealthPoint(self):
        print(f"生命值: {self.healthPoint}")

    def showDamagerPoint(self):
        print(f"伤害值：{self.damagePoint}")

    def beHit(self, lostPoint):
        print(f"遭到植物攻击，生命值损失 {lostPoint} 点")
        self.healthPoint -= lostPoint

z1 = CommonZombie()

print("普通僵尸z1的初始状态：")
z1.showHealthPoint()
z1.showDamagerPoint()

print("普通僵尸z1进入花园...")

z1.beHit(5)
print("当前普通僵尸z1的HP:")
z1.showHealthPoint()

z1.beHit(5)
z1.beHit(5)
print("当前普通僵尸z1的HP:")
z1.showHealthPoint()

z1.beHit(10)
print("当前普通僵尸z1的HP:")