import pygame
from eg07_精灵及精灵组 import *

pygame.init()

# -----------------游戏的初始化------------------
# 创建游戏窗口
# 加载图像数据
screen = pygame.display.set_mode(size=(480, 700))
# 1. 加载图像数据
bg = pygame.image.load("images/background.png")
# 2. blit绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("images/me1.png")
screen.blit(hero, (150, 300))
# 3. update更新屏幕显示
# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("images/enemy1.png")
enemy1 = GameSprite("images/enemy1.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# --------------游戏循环 -> 意味着游戏的正式开始---------------
while True:
    # 指定循环体内部代码的执行频率
    clock.tick(60)  # 设置帧率为60帧
    # 监听用户点击关闭按钮的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 调用quit方法卸载所有的模块
            pygame.quit()
            # exit() 直接终止当前正在运行的进程
            exit()
    # 2. 修改飞机的位置
    hero_rect.y -= 1
    # 一旦飞机整体离开屏幕顶部，则需要强行挪回底部
    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700
    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 重新绘制背景，防止连续的飞机叠加
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # update - 让组中所有的精灵执行各自的update()方法 更新位置
    enemy_group.update()
    # draw - 在screen(canvas)上绘制所有的精灵
    enemy_group.draw(screen)

    # 4. 调用update方法更新显示
    pygame.display.update()
