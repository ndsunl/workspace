import pygame, sys, random, time
# 从pygame模块导入常用的函数和常量
from pygame.locals import *

# 一些全局参数的初始化
def main():
    global FPSCLOCK, DISPLAY, BASICFONT, BLACK, WHITE, RED, GREY

    # 初始化Pygame库
    pygame.init()
    # 初始化一个游戏界面窗口
    DISPLAY = pygame.display.set_mode((640, 480))
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

    playGame()


# 开始游戏
def playGame():
    """初始化贪吃蛇及食物"""

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

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    """游戏主循环"""
    while True:
        # 检测按键等Pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后，退出程序
                pygame.quit()
                sys.exit()

            # 判断键盘事件，用 方向键 或　wsad 来表示上下左右
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.K_w) and direction != DOWN:
                    direction = UP 
                if (event.key == K_DOWN or event.K_s) and direction != UP:
                    direction = DOWN 
                if (event.key == K_LEFT or event.K_a) and direction != RIGHT:
                    direction = LEFT 
                if (event.key == K_RIGHT or event.K_d) and direction != LEFT:
                    direction = RIGHT 

        # 根据键盘的输入，改变蛇的头部，进行转弯操作
        if direction == LEFT:
            snake_Head[0] -= 20
        