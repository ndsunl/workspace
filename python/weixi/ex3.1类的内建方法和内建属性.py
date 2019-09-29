"""
类的内建方法和内建属性
"""

class ConeheadZombie:
    """
    交通锥僵尸类
    属性: ...
    方法: ...
    参数: ...
    """

    def __init__(self):
        self.healtPoint = 60
        self.damagePoint = 5

    def getHealthPoint(self):
        """获取生命值的方法"""
        if self.healtPoint > 0:
            return self.healtPoint
        else:
            return "已经挂了！"

    def getDamagerPoint(self):
        return self.damagePoint

    def beHit(self, lostPoint):
        self.healtPoint -= lostPoint
        return lostPoint

    def __repr__(self):
        return f"一个生命值为 {self.healtPoint} 的交通锥僵尸"

    #def __str__(self):
     #   return f"我是一个生命值为 {self.healtPoint} 的交通锥僵尸"

cz1 = ConeheadZombie()

# 查看对象的所有方法和属性
#print(dir(cz1))

# __str__ 和 __repr__ 方法
print(cz1)

# __class__ 属性
print(f"__class__: {cz1.__class__}")

# __doc__ 属性
print(f"cz1.__doc__: {cz1.__doc__}")
print(f"cz1.getHealthPoint.__doc__: {cz1.getHealthPoint.__doc__}")

# __dict__ 属性
print(f"cz1.__dict__: {cz1.__dict__}")
