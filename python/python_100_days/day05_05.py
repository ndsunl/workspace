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

money = 1000
while money > 0:
    go_on = False
    print()
    print(f"您的总资产为 {money}")
    chip = int(input("请下注: "))
    first = random.randint(1, 6) + random.randint(1, 6)
    print(f"您掷的点数为 {first}")
    if first == 7 or first == 11:
        money += chip
        print("玩家胜!")
    elif first == 2 or first == 3 or first == 12:
        money -= chip
        print("庄家胜!")
    else:
        go_on = True

    while go_on:
        other = random.randint(1, 6) + random.randint(1, 6)
        print(f"您掷的点数为 {other}")
        if other == first:
            money += chip
            print("玩家胜!")
            go_on = False
        elif other == 7:
            money -= chip
            print("庄家胜!")
            go_on = False

print()
print("你的总资产为零，游戏结束!")