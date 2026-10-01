import pygame
import sys

# 1. 파이게임 초기화
pygame.init()

# 2. 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("나만의 2D 카트라이더")

# 3. 사용할 색상 정의 (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GRAY = (100, 100, 100)

# 4. 카트(플레이어) 변수 설정
kart_width = 40
kart_height = 60
kart_x = screen_width // 2 - kart_width // 2
kart_y = screen_height - 100
kart_speed = 7 # 카트의 이동 속도

# 5. 게임을 부드럽게 실행하기 위한 시계 설정
clock = pygame.time.Clock()
running = True

# 6. 메인 게임 루프 (게임이 켜져 있는 동안 계속 반복됨)
while running:
    # (1) 이벤트 처리 (게임 종료 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # (2) 키보드 입력 처리 (방향키)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and kart_x > 0:
        kart_x -= kart_speed
    if keys[pygame.K_RIGHT] and kart_x < screen_width - kart_width:
        kart_x += kart_speed
    if keys[pygame.K_UP] and kart_y > 0:
        kart_y -= kart_speed
    if keys[pygame.K_DOWN] and kart_y < screen_height - kart_height:
        kart_y += kart_speed

    # (3) 화면 그리기
    screen.fill(GRAY) # 아스팔트 느낌의 회색 배경
    
    # 도로 차선 그리기 (디테일 추가!)
    pygame.draw.rect(screen, WHITE, (screen_width//2 - 5, 0, 10, screen_height))
    
    # 내 카트 그리기 (빨간색 직사각형)
    pygame.draw.rect(screen, RED, (kart_x, kart_y, kart_width, kart_height))

    # (4) 지금까지 그린 것을 화면에 업데이트
    pygame.display.update()
    
    # (5) 1초에 60번 화면을 새로고침 (60 FPS)
    clock.tick(60)

# 게임 루프를 빠져나오면 종료
pygame.quit()
sys.exit()