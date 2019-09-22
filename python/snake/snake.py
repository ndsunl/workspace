import pygame, sys, random, time
# 从pygame模块导入常用的函数和常量
from pygame.locals import *

# 初始化Pygame库
pygame.init()
# 初始化一个游戏界面窗口
DISPLAYSURF = pygame.display.set_mode((640, 480))
# 设置游戏窗口的标题
pygame.display.set_caption('人人都是Pythonista - Snake')
# 定义一个变量来控制游戏速度
FPSCLOCK = pygame.time.Clock()
# 初始化游戏界面内使用的字体
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

# 定义颜色变量
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREY = pygame.Color(150, 150, 150)

# 贪吃蛇的初始位置
snake_Head = [100, 100]
# 初始化贪吃蛇的长度（以20*20为一个标准小格子）
snake_Body = [[80, 100], [60, 100], [40, 100]]
# 指定蛇初始前进的方向，向右
direction = "right"

# 给定第一枚食物的位置
food_Position = [300, 300]
# 食物标记：0代表食物已被吃掉；1代表未被吃掉
food_flag = 1