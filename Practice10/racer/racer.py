# Racer Game with Coins
# Controls:
# LEFT arrow  - move left
# RIGHT arrow - move right
# ESC         - quit game

import pygame
import random
import sys
import os
import time


# -------------------- BASIC SETUP --------------------

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font_big = pygame.font.SysFont("Verdana", 55)
font_small = pygame.font.SysFont("Verdana", 20)


# -------------------- FILE LOADING HELPERS --------------------

# This function loads files from racer/resources/
def get_path(filename):
    return os.path.join(os.path.dirname(__file__), "resources", filename)


def load_image(filename, size=None):
    # Load image from resources folder
    image = pygame.image.load(get_path(filename)).convert_alpha()

    # Resize image if needed
    if size is not None:
        image = pygame.transform.scale(image, size)

    return image


# -------------------- LOAD IMAGES AND SOUNDS --------------------

background_img = load_image("AnimatedStreet.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = load_image("Player.png")
enemy_img = load_image("Enemy.png")
coin_img = load_image("coin.png", (35, 35))

# Load and play background music forever
pygame.mixer.music.load(get_path("background.wav"))
pygame.mixer.music.play(-1)

# Load crash sound
crash_sound = pygame.mixer.Sound(get_path("crash.wav"))


# -------------------- GAME VARIABLES --------------------

speed = 5
score = 0
coins_collected = 0

# Background y position for scrolling effect
background_y = 0

# Custom event to increase speed every second
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


# -------------------- PLAYER CLASS --------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Player image and rectangle
        self.image = player_img
        self.rect = self.image.get_rect()

        # Start player near the bottom center
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

        self.speed = 6

    def update(self):
        # Get keyboard state
        keys = pygame.key.get_pressed()

        # Move left and right
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # Do not allow player to leave the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


# -------------------- ENEMY CLASS --------------------

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Enemy image and rectangle
        self.image = enemy_img
        self.rect = self.image.get_rect()

        self.reset_position()

    def reset_position(self):
        # Put enemy above the screen at random x position
        self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.bottom = 0

    def update(self):
        global score

        # Enemy moves down
        self.rect.move_ip(0, speed)

        # If enemy leaves screen, reset it and add score
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            self.reset_position()


# -------------------- COIN CLASS --------------------

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Coin image and rectangle
        self.image = coin_img
        self.rect = self.image.get_rect()

        self.reset_position()

    def reset_position(self):
        # Coin appears randomly above the screen
        self.rect.centerx = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.centery = random.randint(-700, -50)

    def update(self):
        # Coin moves down with the road
        self.rect.move_ip(0, speed)

        # If coin leaves screen, reset it
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


# -------------------- CREATE SPRITES --------------------

player = Player()
enemy = Enemy()

# Group for coins
coins = pygame.sprite.Group()

# Add 3 coins to the game
for _ in range(3):
    coins.add(Coin())

# Group for enemies
enemies = pygame.sprite.Group()
enemies.add(enemy)

# Group for all sprites, used for update and draw
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coins)


# -------------------- GAME OVER FUNCTION --------------------

def game_over():
    # Stop music and play crash sound
    pygame.mixer.music.stop()
    crash_sound.play()

    time.sleep(0.5)

    # Draw red game over screen
    screen.fill(RED)

    game_over_text = font_big.render("Game Over", True, BLACK)
    game_over_rect = game_over_text.get_rect(
        center=(SCREEN_WIDTH // 2, 230)
    )

    score_text = font_small.render(f"Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(
        center=(SCREEN_WIDTH // 2, 310)
    )

    coins_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    coins_rect = coins_text.get_rect(
        center=(SCREEN_WIDTH // 2, 345)
    )

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(coins_text, coins_rect)

    pygame.display.update()

    time.sleep(3)

    pygame.quit()
    sys.exit()


# -------------------- MAIN GAME LOOP --------------------

running = True

while running:
    # -------------------- EVENTS --------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ESC key closes the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Increase game speed every second
        if event.type == INC_SPEED:
            speed += 0.3

    # -------------------- UPDATE SPRITES --------------------
    all_sprites.update()

    # -------------------- COLLISIONS --------------------

    # If player touches enemy, game ends
    if pygame.sprite.spritecollideany(player, enemies):
        game_over()

    # If player touches coins, collect them
    hit_coins = pygame.sprite.spritecollide(player, coins, False)

    for coin in hit_coins:
        coins_collected += 1
        coin.reset_position()

    # -------------------- DRAW BACKGROUND --------------------

    # Move background down
    background_y += speed

    # Reset background when it moves one full screen
    if background_y >= SCREEN_HEIGHT:
        background_y = 0

    # Draw two backgrounds for smooth infinite scrolling
    screen.blit(background_img, (0, background_y))
    screen.blit(background_img, (0, background_y - SCREEN_HEIGHT))

    # -------------------- DRAW SPRITES --------------------
    all_sprites.draw(screen)

    # -------------------- DRAW TEXT --------------------

    # Score top left
    score_surface = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (10, 10))

    # Speed under score
    speed_surface = font_small.render(f"Speed: {speed:.1f}", True, BLACK)
    screen.blit(speed_surface, (10, 35))

    # Coins top right
    coin_surface = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    coin_rect = coin_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(coin_surface, coin_rect)

    # Update display
    pygame.display.update()

    # Limit FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()