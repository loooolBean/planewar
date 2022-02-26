import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口大小
screen = pygame.display.set_mode((480, 700))
# 创建时钟对象
clock = pygame.time.Clock()

# 绘制背景图像
# 1>加载背景图像
bg = pygame.image.load("./images/background.png")
# 2>绘制图像
screen.blit(bg, (0, 0))
# 3>更新屏幕显示
# pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))  # blit方法第二个参数可以传入一个元组也可以传入一个矩形对象
pygame.display.update()

i = 0

# 游戏循环
while True:

    # 调用tick方法，每秒执行60次
    clock.tick(60)
    print(i)
    i += 1

pygame.quit()
