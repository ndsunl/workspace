"""
普通僵尸类
"""

class CommonZombie:

    def __init__(self):
        self.healthPoint = 30           # 生命值 HP
        self.damagePoint = 5            # 伤害值 DP

    def showHealthPoint(self):
        print(f"生命值: {self.healthPoint}")

    def show