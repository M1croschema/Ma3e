from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 420:
            self.direction = "right"
        if self.rect.x >= win_width - 105:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(0, 0, 0, 20, 20, 640, 10)
w2 = Wall(0, 0, 0, 90, 140, 10, 340)
w3 = Wall(0, 0, 0, 180, 20, 10, 340)
w4 = Wall(0, 0, 0, 270, 140, 10, 250)
w5 = Wall(0, 0, 0, 270, 140, 250, 10)
w6 = Wall(0, 0, 0, 520, 140, 10, 340)
w7 = Wall(0, 0, 0, 660, 20, 10, 450)
w8 = Wall(0, 0, 0, 270, 300, 160, 10)


win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("fon.jpg"), (win_width, win_height))

player = Player("hero3.png", 5, win_height - 80, 4)
monster = Enemy("kit.png", win_width - 80,280, 4)
dop_nagoroda = GameSprite("CNR.png", 270, 140, 4)
final = GameSprite("CNR.png", win_width - 120, win_height - 80, 0)

font.init()
font = font.SysFont("Arial", 70)
dop_nag = font.render('Доп нагорода!', True, (255, 215, 0))
win = font.render('Ти переміг!', True, (255, 215, 0))
lose = font.render('Ти програв!', True, (180, 0, 0))

game = True
clock = time.Clock()
FPS = 60
finish = False

mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()

kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        dop_nagoroda.update()
        player.reset()
        monster.reset()
        dop_nagoroda.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        if sprite.collide_rect(player, dop_nagoroda):
            window.blit(dop_nag, (50, 200))
            dop_nagoroda.rect.x = 500
            dop_nagoroda.rect.y = 500



        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))


    display.update()
    clock.tick(FPS)