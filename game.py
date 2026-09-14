import pygame

import math

from setting import WIDTH, HEIGHT, SPEED, FPS, DIFFICULTIES

from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.snake = Snake()
        self.food = Food(self.snake.size, self.snake.body)

        self.score = 0
        self.high_score = self.load_high_score()

        self.font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 20)
        self.game_over_font = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40)

        self.state = "menu"

        self.move_timer = 0
        self.game_over_timer = 0
        self.menu_timer = 0

        self.speed = SPEED

        self.difficulties = list(DIFFICULTIES.keys())
        self.selected_difficulty = 0

        self.menu_snake_x = 100
        self.menu_snake_y = 100
        self.menu_snake_speed = 100
        self.menu_snake2_x = 700
        self.menu_snake2_y = 500
        self.menu_snake2_speed = -70

        self.menu_bg = pygame.image.load("assets/background.jpeg").convert()
        self.menu_bg = pygame.transform.scale(self.menu_bg, (WIDTH, HEIGHT))
        self.difficulty_bg = pygame.image.load("assets/back.jpeg").convert()
        self.difficulty_bg = pygame.transform.scale(self.difficulty_bg, (WIDTH, HEIGHT))
        self.trophy_image = pygame.image.load("assets/trophy.png").convert_alpha()
        self.trophy_image = pygame.transform.scale(self.trophy_image, (30, 40))
        self.start_image = pygame.image.load("assets/start.png").convert_alpha()
        self.start_image = pygame.transform.scale(self.start_image, (320, 100))
        self.difficulty_image = pygame.image.load("assets/difficulty.png").convert_alpha()
        self.difficulty_image = pygame.transform.scale(self.difficulty_image, (320, 100))
        self.retour_image = pygame.image.load("assets/retour.png").convert_alpha()
        self.retour_image = pygame.transform.scale(self.retour_image, (320, 100))

        self.start_rect = pygame.Rect(0, 0, 320, 100)
        self.difficulty_rect = pygame.Rect(0, 0, 320, 100)
        self.back_rect = pygame.Rect(0, 0, 320, 100)

        self.difficulty_rects = []

    def load_high_score(self):
        with open("high_score.txt", "r") as file:
            return int(file.read())

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def draw_menu(self):
        # background
        self.screen.blit(self.menu_bg, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120)) 
        self.screen.blit(overlay, (0, 0))

        # Meilleur score
        high_score_text = self.font.render(
            f"Meilleur score : {self.high_score}",
            True,
            "yellow"
        )

        high_score_rect = high_score_text.get_rect(
            center=(WIDTH // 2, 150)
        )

        # Icone Trophy
        trophy_rect = self.trophy_image.get_rect(
            midright=(high_score_rect.left - 10, high_score_rect.centery)
        )

        self.screen.blit(
            self.trophy_image,
            trophy_rect
        )

        self.screen.blit(high_score_text, high_score_rect)

        # Bouton Start
        self.start_rect = self.start_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        self.screen.blit(self.start_image, self.start_rect)

        self.difficulty_rect = self.difficulty_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        self.screen.blit(self.difficulty_image, self.difficulty_rect)

        difficulty = self.difficulties[self.selected_difficulty]

        difficulty_text = self.font.render(
            f"Difficulté : {difficulty.upper()}",
            True,
            "yellow"
        )

        difficulty_rect = difficulty_text.get_rect(
            center=(WIDTH // 2, HEIGHT - 130)
        )

        self.screen.blit(
            difficulty_text,
            difficulty_rect
        )

    def draw_score(self):
        text = self.font.render(
            f"Score : {self.score}",
            True,
            "white"
        )

        self.screen.blit(text, (10, 10))

    def draw_difficulty(self):
        self.difficulty_rects = []
        self.screen.blit(self.difficulty_bg, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120)) 
        self.screen.blit(overlay, (0, 0))

        for i, difficulty in enumerate(self.difficulties):

            color = "yellow" if i == self.selected_difficulty else "white"
            indicator = ">" if i == self.selected_difficulty else " "

            text = self.font.render(
                f"{indicator} {difficulty.upper()}",
                True,
                color
            )

            rect = text.get_rect(
                center=(
                    WIDTH // 2,
                    220 + i * 60
                )
            )

            self.difficulty_rects.append(rect)

            self.screen.blit(text, rect)

        # Bouton Retour
        self.back_rect = self.retour_image.get_rect(center=(WIDTH // 2, HEIGHT - 130))

        self.screen.blit(self.retour_image, self.back_rect)

    def update(self):
        next_position = self.snake.next_position()

        if self.check_wall_collision(next_position):
            self.state = "game_over"

            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()

            self.game_over_timer = 0

            return

        if next_position == self.food.position:
            self.snake.move(grow=True)
            self.food.position = self.food.random_position(self.snake.body)
            self.score += 1
        else:
            self.snake.move()

        if self.check_self_collision():
            self.state = "game_over"

            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()

            self.game_over_timer = 0

    def draw_game_over(self):

        # Panneau central
        panel_width = 500
        panel_height = 400

        panel_rect = pygame.Rect(
            WIDTH // 2 - panel_width // 2,
            HEIGHT // 2 - panel_height // 2,
            panel_width,
            panel_height
        )

        pygame.draw.rect(
            self.screen,
            "black",
            panel_rect
        )

        pygame.draw.rect(
            self.screen,
            "red",
            panel_rect,
            4
        )

        letters = int(self.game_over_timer * 10)

        text = "GAME OVER"[:letters]

        if text:
            game_over_text = self.game_over_font.render(text, True, "red")
        else:
            game_over_text = pygame.Surface((0, 0))

        rect = game_over_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 80)
        )

        self.screen.blit(game_over_text, rect)

        # Petits losanges décoratifs
        pygame.draw.polygon(
            self.screen,
            "red",
            [
                (rect.left - 40, rect.centery),
                (rect.left - 30, rect.centery - 10),
                (rect.left - 20, rect.centery),
                (rect.left - 30, rect.centery + 10)
            ]
        )

        pygame.draw.polygon(
            self.screen,
            "red",
            [
                (rect.right + 20, rect.centery),
                (rect.right + 30, rect.centery - 10),
                (rect.right + 40, rect.centery),
                (rect.right + 30, rect.centery + 10)
            ]
        )

        if self.game_over_timer >= 1.3:
            # Score
            score_text = self.font.render(
                f"Score : {self.score}",
                True,
                "white"
            )

            score_rect = score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2)
            )

            self.screen.blit(score_text, score_rect)

        if self.game_over_timer >= 1.8:
            # High Score
            high_score_text = self.font.render(
                f"Meilleur Score : {self.high_score}",
                True,
                "yellow"
            )

            high_score_rect = high_score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 40)
            )

            # Icone Trophy
            trophy_rect = self.trophy_image.get_rect(
                midright=(high_score_rect.left - 10, high_score_rect.centery)
            )

            self.screen.blit(
                self.trophy_image,
                trophy_rect
            )

            self.screen.blit(high_score_text, high_score_rect)

        if self.game_over_timer >= 2.3:
            # Instructions
            instructions_text = self.font.render(
                "[R] REJOUER    [M] MENU",
                True,
                "white"
            )

            instructions_rect = instructions_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 100)
            )

            self.screen.blit(instructions_text, instructions_rect)

    def check_wall_collision(self, position):
        x, y = position

        size = self.snake.size

        return (
            x < 0
            or x + size > WIDTH
            or y < 0
            or y + size > HEIGHT
        )

    def check_self_collision(self):
        head = self.snake.get_head()

        return head in self.snake.body[1:]

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.snake.size, self.snake.body)
        self.score = 0
        self.move_timer = 0
        self.state = "playing"

    def run(self):
        while self.running:
            # 1. Événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.state == "menu":
                            if self.start_rect.collidepoint(event.pos):
                                self.state = "playing"

                            if self.difficulty_rect.collidepoint(event.pos):
                                self.state = "difficulty"

                        elif self.state == "difficulty":
                            for i, rect in enumerate(self.difficulty_rects):
                                if rect.collidepoint(event.pos):
                                    self.selected_difficulty = i

                                    difficulty = self.difficulties[i]
                                    self.speed = DIFFICULTIES[difficulty]

                                    self.state = "menu"
                                    break
                            if self.back_rect.collidepoint(event.pos):
                                self.state = "menu"

                if event.type == pygame.KEYDOWN:
                    
                    # MENU
                    if self.state == "menu":
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            self.state = "playing"

                    # DIFFICULTY
                    elif self.state == "difficulty":
                        if event.key == pygame.K_UP:
                            self.selected_difficulty = max(
                                0,
                                self.selected_difficulty - 1
                            )

                        elif event.key == pygame.K_DOWN:
                            self.selected_difficulty = min(
                                len(self.difficulties) - 1,
                                self.selected_difficulty + 1
                            )

                        elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            difficulty = self.difficulties[self.selected_difficulty]
                            self.speed = DIFFICULTIES[difficulty]
                            self.state = "menu"

                        elif event.key == pygame.K_ESCAPE:
                            self.state = "menu"

                    # JEU
                    elif self.state == "playing":
                        if event.key == pygame.K_UP:
                            self.snake.change_direction(0, -1)

                        elif event.key == pygame.K_DOWN:
                            self.snake.change_direction(0, 1)

                        elif event.key == pygame.K_LEFT:
                            self.snake.change_direction(-1, 0)

                        elif event.key == pygame.K_RIGHT:
                            self.snake.change_direction(1, 0)

                    # GAME OVER
                    elif self.state == "game_over":
                        if event.key == pygame.K_r:
                            self.reset()

                        elif event.key == pygame.K_m:
                            self.reset()
                            self.state = "menu"

            dt = self.clock.tick(FPS) / 1000 # temps écoulé depuis la dernière frame en secondes

            if self.state == "playing":
                self.move_timer += dt
                if self.move_timer >= 1 / self.speed:
                    self.update() # 2. Mise à jour
                    self.move_timer = 0

            if self.state == "game_over":
                self.game_over_timer += dt

            # 3. Affichage
            self.screen.fill("purple")

            if self.state == "menu":
                self.draw_menu()

            elif self.state == "playing":
                self.snake.draw(self.screen)
                self.food.draw(self.screen)
                self.draw_score()

            elif self.state == "game_over":
                    # Le serpent clignote pendant les premières secondes
                if self.game_over_timer < 0.8:
                    if int(self.game_over_timer * 10) % 2 == 0:
                        self.snake.draw(self.screen)

                self.draw_game_over()

            elif self.state == "difficulty":
                self.draw_difficulty()

            pygame.display.flip()

        pygame.quit()