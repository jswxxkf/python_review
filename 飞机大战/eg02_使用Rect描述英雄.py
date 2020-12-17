import pygame

# 加载初始化所有模块
pygame.init()

# 使用Rect描述英雄
hero_rect = pygame.Rect((100, 500, 120, 125))
print("英雄的原点：{} {}".format(hero_rect.x, hero_rect.y))
print("英雄的尺寸：%d %d" % hero_rect.size)

# 退出游戏前，卸载所有pygame模块
pygame.quit()
