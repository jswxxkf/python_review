import pygame

pygame.init()

# ----------------游戏的初始化------------------
# 创建游戏窗口
# 加载图像数据
screen = pygame.display.set_mode(size=(480, 700))
# 1. 加载图像数据
bg = pygame.image.load("images/background.png")
# 2. blit绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("images/me1.png")
screen.blit(hero, (150, 500))
# 3. update更新屏幕显示
# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
i = 0
# --------------游戏循环 -> 意味着游戏的正式开始---------------
while True:
    # 指定循环体内部代码的执行频率
    clock.tick(60)  # 设置帧率为60帧
    print(i)
    i += 1

pygame.quit()
