import time
import pygame
import random

WIDTH = 800
HEIGHT  = 600
skor = 0
skor_2 = 0
vurma = 0
boss_vurma = 0
boss_yenme = 0
level = 1
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

    def show_game_over(self):
        font = pygame.font.SysFont("arial", 32)
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(game_over_text, game_over_rect)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption("Uzay Savaşı")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        print("You lost!")
        break
    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for bullet_hit in bullet_hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        skor += 1
        vurma += 1
        skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))

    if skor >= 100:
        running = False
        print("You won!","New level is unlocked!","Angry enemies are comming!!","Are you ready?")
        level += 1
        skor_2 += 1
    screen.fill('white')
    all_sprites.draw(screen)
    font = pygame.font.SysFont("arial", 32)
    skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))
    skor_metni_koordinati = skor_metni.get_rect()
    skor_metni_koordinati.center = (50,50)
    screen.blit(skor_metni, skor_metni_koordinati)
    pygame.display.update()



pygame.quit()
time.sleep(2)

WIDTH = 800
HEIGHT = 600
skor = 0
level = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy(1).png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(5, 12)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption("Uzay Savaşı")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        print("You lost!")

    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for bullet_hit in bullet_hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        skor += 1
        vurma += 1
        skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))

    if skor >= 50:
        running = False
        print("You won!","New level is unlocked!","Angry enemies are comming!!","Are you ready?")
        level += 1
        skor_2 += 1
    screen.fill('white')
    all_sprites.draw(screen)
    font = pygame.font.SysFont("arial", 32)
    skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))
    skor_metni_koordinati = skor_metni.get_rect()
    skor_metni_koordinati.center = (50,50)
    screen.blit(skor_metni, skor_metni_koordinati)
    pygame.display.update()



pygame.quit()
time.sleep(2)
WIDTH = 800
HEIGHT = 600
skor = 0
level = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy(2).png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(13,15)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption("Uzay Savaşı")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        print("You lost!")

        break
    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for bullet_hit in bullet_hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        skor += 1
        vurma += 1
        skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))

    if skor >= 20:
        running = False
        print("You won!!!!")
        print("You won!", "New level is unlocked!", "Angry enemies are comming!!", "Are you ready?")
        skor_2 += 1
    screen.fill('white')
    all_sprites.draw(screen)
    font = pygame.font.SysFont("arial", 32)
    skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))
    skor_metni_koordinati = skor_metni.get_rect()
    skor_metni_koordinati.center = (50,50)
    screen.blit(skor_metni, skor_metni_koordinati)
    pygame.display.update()


pygame.quit()

time.sleep(2)
WIDTH = 800
HEIGHT = 600
skor = 0
level = 4
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy(3).png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(15,17)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption("Uzay Savaşı")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        print("You lost!")

        break
    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for bullet_hit in bullet_hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        skor += 1
        vurma += 1
        skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))

    if skor >= 20:
        running = False
        print("You won!!!!")
        print("You won!", "New level is unlocked!", "Angry enemies are comming!!", "Are you ready?",'Boss is coming!!')
        skor_2 += 1
    screen.fill('white')
    all_sprites.draw(screen)
    font = pygame.font.SysFont("arial", 32)
    skor_metni = font.render("Skor:" + str(skor), True, (0, 0, 0))
    skor_metni_koordinati = skor_metni.get_rect()
    skor_metni_koordinati.center = (50,50)
    screen.blit(skor_metni, skor_metni_koordinati)
    pygame.display.update()


pygame.quit()
print(f'Kazandığınız toplam oyun sayısı: {skor_2} tebrikler!! ')
print(f'Toplam vurduğunuz düşman sayısı: {vurma} tebrikler!!'  )

time.sleep(2)
WIDTH = 800
HEIGHT = 600
skor = 0
skor_2 = 0
vurma = 0
level = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("creepy-ghost.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4)
        self.health = 100

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10
        self.strength = 20

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Uzay Savaşı")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy = Enemy()
all_sprites.add(enemy)
enemies.add(enemy)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
        print("You lost!")
        break

    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
    for bullet, enemy_list in bullet_hits.items():
        for enemy in enemy_list:
            enemy.health -= bullet.strength
            if enemy.health <= 0:
                enemy.kill()
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)
                skor += 1
                boss_vurma += 1
                print(f"You destroyed a boss!!")

    if skor >= 1:
        boss_yenme += 1
        running = False
        print("You won!")
        break

    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()

print(f'Yendiğiniz toplam boss sayısı: {boss_yenme} tebrikler!! ')
print(f'Toplam vurduğunuz boss sayısı: {boss_vurma} tebrikler!!'  )




