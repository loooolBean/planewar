import pygame
from plane_sprites import *

# 游戏的初始化
pygame.init()

# 创建游戏窗口大小
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>加载背景图像
bg = pygame.image.load("./images/background.png")
# 2>绘制图像
screen.blit(bg, (0, 0))
# 3>更新屏幕显示
pygame.display.update()

# 绘制英雄飞机
# 加载飞机图像
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (200, 500))  # blit方法第二个参数可以传入一个元组也可以传入一个矩形对象
# pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png")

# 创建敌机精灵组
enemy_group = pygame.sprite.Group((enemy, enemy1))

# 游戏循环
while True:

    # 调用tick方法，每秒执行60次
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 调用quit方法
            pygame.quit()

            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.使用bilt方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法，update和draw
    # update
    enemy_group.update()
    # draw
    enemy_group.draw(screen)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()
