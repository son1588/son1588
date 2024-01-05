import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Ball")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Kích thước và vị trí của quả bóng
ball_size = 50
ball_x = random.randint(0, width - ball_size)
ball_y = 0

# Tốc độ rơi của quả bóng
fall_speed = 5

# Điểm số
score = 0

# Chạy trò chơi
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển quả bóng xuống dưới
    ball_y += fall_speed

    # Kiểm tra nếu quả bóng chạm đáy màn hình
    if ball_y > height:
        ball_y = 0
        ball_x = random.randint(0, width - ball_size)
        score += 1

    # Vẽ màn hình
    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x + ball_size // 2, int(ball_y)), ball_size // 2)

    # Vẽ điểm số
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn tốc độ khung hình
    clock.tick(30)