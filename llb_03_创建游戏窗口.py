import pygame

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

while True:
    pass

pygame.quit()
