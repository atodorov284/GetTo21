import sys
import time

import pygame
from Game import *

pygame.init()
size = width, height = 600, 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
game = GameSticks('first')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    if (user is None):
        # Title
        title = largeFont.render("Play Get To 21", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)
        pos = 0

        # Draw buttons
        playFirstButton = pygame.Rect((width / 8), (height / 2), width / 3, 50)
        playFirst = mediumFont.render("Play First", True, black)
        playFirstRect = playFirst.get_rect()
        playFirstRect.center = playFirstButton.center
        pygame.draw.rect(screen, white, playFirstButton)
        screen.blit(playFirst, playFirstRect)

        playSecondButton = pygame.Rect(5 * (width / 8), (height / 2), width / 3, 50)
        playSecond = mediumFont.render("Play Second", True, black)
        playSecondRect = playSecond.get_rect()
        playSecondRect.center = playSecondButton.center
        pygame.draw.rect(screen, white, playSecondButton)
        screen.blit(playSecond, playSecondRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playFirstButton.collidepoint(mouse):
                time.sleep(0.2)
                game = GameSticks('first')
                time.sleep(0.5)
                user = 'player'
            elif playSecondButton.collidepoint(mouse):
                time.sleep(0.2)
                game = GameSticks('second')
                time.sleep(0.5)
                user = 'ai'
    else:
        # Draw game board
        screen.fill(black)
        tile_size = 25
        tile_origin = (width / 3 - (1.5 * tile_size) - 100,
                       height / 2 - (1.5 * tile_size))
        tiles = []
        row = []
        for j in range(21):
            rect = pygame.Rect(
                tile_origin[0] + j * tile_size,
                tile_origin[1] + tile_size - 30,
                tile_size, tile_size + 75
            )
            pygame.draw.rect(screen, white, rect, 3)
            row.append(rect)
        tiles.append(row)
        image = pygame.image.load(r'Match-0.png')

        game_over = not game.End()

        if not game_over:
            if user == 'ai':
                title = f"Computer thinking..."
                time.sleep(1)
                sticks = game.ai()
                game.Play(sticks, 'ai')
                pos += sticks
                user = 'player'
            else:
                # Choose 1 stick
                one_stick_button = pygame.Rect((width / 10), (height / 1.3), width / 4 - 10, 40)
                one_stick = mediumFont.render("1 Stick", True, black)
                one_stick_rect = one_stick.get_rect()
                one_stick_rect.center = one_stick_button.center
                pygame.draw.rect(screen, white, one_stick_button)
                screen.blit(one_stick, one_stick_rect)

                # Choose 2 sticks
                two_sticks_button = pygame.Rect((width / 10 + 200), (height / 1.3), width / 4 - 10, 40)
                two_sticks = mediumFont.render("2 Sticks", True, black)
                two_sticks_rect = two_sticks.get_rect()
                two_sticks_rect.center = two_sticks_button.center
                pygame.draw.rect(screen, white, two_sticks_button)
                screen.blit(two_sticks, two_sticks_rect)

                # Choose 3 sticks
                three_sticks_button = pygame.Rect((width / 10 + 390), (height / 1.3), width / 4 - 10, 40)
                three_sticks = mediumFont.render("3 Sticks", True, black)
                three_sticks_rect = three_sticks.get_rect()
                three_sticks_rect.center = three_sticks_button.center
                pygame.draw.rect(screen, white, three_sticks_button)
                screen.blit(three_sticks, three_sticks_rect)

                # Check if button is pressed
                click, _, _ = pygame.mouse.get_pressed()
                if click == 1 and user == 'player' and not game_over:
                    mouse = pygame.mouse.get_pos()
                    if one_stick_button.collidepoint(mouse):
                        time.sleep(0.2)
                        game.Play(1, 'player')
                        pos += 1
                        user = 'ai'
                    elif two_sticks_button.collidepoint(mouse):
                        time.sleep(0.2)
                        game.Play(2, 'player')
                        pos += 2
                        user = 'ai'
                    elif three_sticks_button.collidepoint(mouse):
                        time.sleep(0.2)
                        game.Play(3, 'player')
                        pos += 3
                        user = 'ai'
        if game_over:
            winner = game.Winner()
            title = 'AI wins.' if winner == 'ai' else 'You win!'
        elif user == 'player':
            title = f"Your turn."
        elif user == 'ai':
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)
        for i in range(pos):
            if i < 21:
                screen.blit(image, (i * 25 + 65, 160))
        total = f'Total: {game.sticks}'
        total = largeFont.render(total, True, white)
        totalRect = total.get_rect()
        totalRect.center = (width / 2, 100)
        screen.blit(total, totalRect)

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    game = None
                    ai_turn = False

    pygame.display.flip()
