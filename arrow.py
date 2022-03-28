import sys
import pygame
import random

pygame.init()

ARROW_SYMBOLS = ['↑', '↓', '←', '→']
CHOICES = ['up', 'down', 'left', 'right']

arrow_dict = {
    'up': '↑',
    'down': '↓',
    'left': '←',
    'right': '→'
}

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)
C_BRONZE = (120, 120, 0)
C_DARKBLUE = (0, 0, 50)
C_DARKGREEN = (0, 50, 0)

DIS_WIDTH, DIS_HEIGHT = 600, 600
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Arrows!")


class Game:
    def __init__(self):
        self.current = ''
        self.current_symbol = ''
        self.player_choice = ''
        self.score = 0
        self.highscore = 0

    def choice(self):
        self.current = random.choice(CHOICES)
        self.current_symbol = arrow_dict[self.current]
        print(self.current, self.current_symbol)

    def check(self):
        if self.player_choice == '':
            pass
        elif self.player_choice == self.current:
            draw.barx = 100
            self.player_choice = ''
            self.score += 1
            draw.bar_speed += .1
            self.choice()
        else:
            gameover()

    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score


class Draw:
    def __init__(self):
        self.symbol_font = pygame.font.Font('seguisym.ttf', 200)
        self.letter_font = pygame.font.Font('seguisym.ttf', 100)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.bar_speed = .1
        self.barx = 100

    def symbol(self, a):
        if a == 'symbol':
            sym = self.symbol_font.render(game.current_symbol, True, C_WHITE)
            dis.blit(sym, (200, 80))
        else:
            sym = self.letter_font.render(game.current.upper(), True, C_WHITE)
            dis.blit(sym, (200, 150))

    def time_bar(self):
        pygame.draw.rect(dis, C_GREEN, (self.barx, 400, 400, 50))  # time bar

        pygame.draw.rect(dis, C_BLACK, (0, 0, DIS_WIDTH, 400))  # top border
        pygame.draw.rect(dis, C_BLACK, (0, 450, DIS_WIDTH, 300))  # bottom border
        pygame.draw.rect(dis, C_BLACK, (0, 400, 100, 50))  # right border
        pygame.draw.rect(dis, C_BLACK, (500, 400, 100, 50))  # left border

        self.barx -= self.bar_speed

        if self.barx < -300:
            gameover()

    def score(self):
        dis.blit(self.font.render(f"Score: {game.score}", True, C_WHITE), (10, 10))

    def start_screen(self, col):
        dis.blit(self.letter_font.render("Arrows!", True, C_BRONZE), (135, 25))
        dis.blit(self.symbol_font.render('↑ ↓←→', True, C_WHITE), (8, 100))
        pygame.draw.rect(dis, col, (225, 400, 150, 50))
        dis.blit(self.font.render("START", True, C_WHITE), (245, 410))

    def gameover_screen(self):
        dis.blit(pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, C_WHITE), (100, 250))
        dis.blit(self.font.render(f"Highscore: {game.highscore}", True, C_WHITE), (200, 325))
        dis.blit(pygame.font.Font('freesansbold.ttf', 15).render("Press [SPACE] to retry", True, C_WHITE), (215, 550))


game = Game()
draw = Draw()


def game_loop():
    nxt = True
    running = True
    while running:

        dis.fill(C_RED)
        draw.time_bar()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                nxt = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.player_choice = 'up'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.player_choice = 'down'
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.player_choice = 'left'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.player_choice = 'right'
                else:
                    nxt = False
                    gameover()

        if game.current == '':
            game.choice()

        game.check()
        game.check_highscore()

        if nxt:
            a = random.choice(['letter', 'symbol'])
            nxt = False
        draw.symbol(a)

        draw.score()

        pygame.display.update()


def gameover():
    while True:
        dis.fill(C_BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw.barx = 100
                    draw.bar_speed = .1
                    game.player_choice = ''
                    game.score = 0
                    game_loop()

        draw.gameover_screen()
        draw.score()

        pygame.display.update()


def startgame():
    while True:
        dis.fill(C_BLACK)
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if mousex in range(225, 376) and mousey in range(400, 451):
                col = C_BRONZE
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_loop()
            else:
                col = C_DARKGREEN

        draw.start_screen(col)

        pygame.display.update()


startgame()
