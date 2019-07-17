"""
craps赌博游戏

规则：
1. 玩家掷两个骰子，每个骰子点数为1-6
2. 如果第一次点数和为7或11，则玩家胜
   如果点数和为2、3或12，则玩家输庄家胜
3. 若和为其他点数，则记录第一次的点数和
   玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜
   若掷出的点数和为7则庄家胜

Version: 0.1
Author: ndsunl
"""

import random

print("你的总资产为 1000")
money = 1000
chip = int(input("请下注: "))
first = random.randint(1, 6) + random.randint(1, 6)
if first == 7 or first == 11:
    money += chip
    print(f"玩家胜，您的筹码为 {money}")
elif first == 2 or first == 3 or first == 12:
    money -= chip
    print(f"庄家胜，您的筹码为 {money}")
else:    