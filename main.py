import pygame
import random

GENISLIK = 800
YUKSEKLIK = 600
FPS = 60

BEYAZ = (255, 255, 255)
KIRMIZI = (255, 0, 0)
MAVI = (0, 0, 255)

pygame.init()
pygame.mixer.init()
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Canavar Avı")
saat = pygame.time.Clock()

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, oyuncu_numarasi):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assasin.png".format(oyuncu_numarasi)).convert()
        self.image.set_colorkey(BEYAZ)
        self.rect = self.image.get_rect()
        self.rect.center = (GENISLIK / 2, YUKSEKLIK / 2)
        self.oyuncu_numarasi = oyuncu_numarasi

    def update(self):
        tuslar = pygame.key.get_pressed()
        if self.oyuncu_numarasi == 1:
            if tuslar[pygame.K_LEFT]:
                self.rect.x -= 5
            if tuslar[pygame.K_RIGHT]:
                self.rect.x += 5
            if tuslar[pygame.K_UP]:
                self.rect.y -= 5
            if tuslar[pygame.K_DOWN]:
                self.rect.y += 5
        elif self.oyuncu_numarasi == 2:
            if tuslar[pygame.K_a]:
                self.rect.x -= 5
            if tuslar[pygame.K_d]:
                self.rect.x += 5
            if tuslar[pygame.K_w]:
                self.rect.y -= 5
            if tuslar[pygame.K_s]:
                self.rect.y += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GENISLIK:
            self.rect.right = GENISLIK
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > YUKSEKLIK:
            self.rect.bottom = YUKSEKLIK

class Canavar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("monster (1).png").convert()
        self.image.set_colorkey(BEYAZ)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(GENISLIK - self.rect.width)
        self.rect.y = random.randrange(YUKSEKLIK - self.rect.height)

    def update(self):
        pass

tum_spritelar = pygame.sprite.Group()
canavarlar = pygame.sprite.Group()
oyuncular = pygame.sprite.Group()

oyuncu1 = Oyuncu(1)
oyuncu2 = Oyuncu(2)
tum_spritelar.add(oyuncu1)
tum_spritelar.add(oyuncu2)
oyuncular.add(oyuncu1)
oyuncular.add(oyuncu2)

for i in range(100):
    canavar = Canavar()
    tum_spritelar.add(canavar)
    canavarlar.add(canavar)

skor1 = 0
skor2 = 0

oyun_bitir = False
baslangic_zamani = pygame.time.get_ticks()
oyun_zamani = 20

while not oyun_bitir:
    saat.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_bitir = True

    gecerli_zaman = round((pygame.time.get_ticks() - baslangic_zamani) / 1000)
    if gecerli_zaman > oyun_zamani:
        oyun_bitir = True

    tum_spritelar.update()

    oyuncu1_vurulan_canavarlar = pygame.sprite.spritecollide(oyuncu1, canavarlar, False)
    for canavar in oyuncu1_vurulan_canavarlar:
        skor1 += 1
        canavar.kill()

    oyuncu2_vurulan_canavarlar = pygame.sprite.spritecollide(oyuncu2, canavarlar, False)
    for canavar in oyuncu2_vurulan_canavarlar:
        skor2 += 1
        canavar.kill()

    ekran.fill(MAVI)
    tum_spritelar.draw(ekran)
    pygame.draw.rect(ekran, BEYAZ, (10, 10, (oyun_zamani - gecerli_zaman) * 40, 25))
    pygame.display.flip()

pygame.quit()
print("Oyuncu 1: {} Canavar".format(skor1))
print("Oyuncu 2: {} Canavar".format(skor2))
if skor1 > skor2:
    print("Oyuncu 1 kazandı!!!!!")
elif skor2 > skor1:
    print("Oyuncu 2 kazandı!!!!!")
else:
    print("Berabere")
    

