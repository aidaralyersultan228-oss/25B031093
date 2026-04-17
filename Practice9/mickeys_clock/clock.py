import os
import math
import datetime
import pygame


def rotate_hand(screen, image, center, angle, scale_size, radius):
    hand = pygame.transform.scale(image, scale_size)
    rotated = pygame.transform.rotate(hand, -angle)

    angle_rad = math.radians(angle)
    end_x = center[0] + radius * math.sin(angle_rad)
    end_y = center[1] - radius * math.cos(angle_rad)

    rect = rotated.get_rect(center=((center[0] + end_x) / 2, (center[1] + end_y) / 2))
    screen.blit(rotated, rect)


def run_clock():
    pygame.init()

    WIDTH = 900
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Clock")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 32)

    base_path = os.path.dirname(__file__)
    images_path = os.path.join(base_path, "images")

    bg = pygame.image.load(os.path.join(images_path, "clock.png")).convert_alpha()
    left_hand = pygame.image.load(os.path.join(images_path, "left_hand.png")).convert_alpha()
    right_hand = pygame.image.load(os.path.join(images_path, "right_hand.png")).convert_alpha()

    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    center = (WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        minute_angle = minutes * 6 + seconds * 0.1
        second_angle = seconds * 6

        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))

        rotate_hand(
            screen,
            left_hand,
            center,
            minute_angle,
            (100, 400),
            100
        )

        rotate_hand(
            screen,
            right_hand,
            center,
            second_angle,
            (700, 1000),
            150
        )

        time_text = font.render(f"{minutes:02d}:{seconds:02d}", True, (0, 0, 0))
        screen.blit(time_text, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()