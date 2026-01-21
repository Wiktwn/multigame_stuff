import pygame
import os

from functions import cleanup_time
import connect4, pygame_checkers, pygame_chess

connect4.use_as_module = True
pygame_checkers.use_as_module = True
pygame_chess.use_as_module = True

pygame.init()

playing_chess = False
playing_checkers = False
playing_connect4 = False
game_vals = [playing_chess, playing_checkers, playing_connect4]
menu_screen_width = 800
menu_screen_height = 800
screen = pygame.display.set_mode((menu_screen_width, menu_screen_height), pygame.RESIZABLE)
font = pygame.font.Font(None, 48)
frm = pygame.time.Clock()

chess_icon = pygame.image.load("chess_icon.png")
chess_icon = pygame.transform.scale_by(chess_icon, .1)
checkers_icon = pygame.image.load("checkers_icon.png")
checkers_icon = pygame.transform.scale_by(checkers_icon, .15)
connect4_icon = pygame.image.load("connect4_icon.png")
connect4_icon = pygame.transform.scale_by(connect4_icon, .27)

chess_button = checkers_icon.get_rect(center=(800/6,400))
checkers_button = checkers_icon.get_rect(center=(800/2,400))
connect4_button = connect4_icon.get_rect(center=(800*5/6, 400))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0) # exit while loop
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
        
            if pygame.Rect.collidepoint(chess_button, mouse):
                print("Load Chess")
                pygame_chess.entrypoint() # pass control of the window to the chess module
                
            elif pygame.Rect.collidepoint(checkers_button, mouse):
                print("Load Checkers")
                pygame_checkers.entrypoint() # pass control of the window to the checkers module
                
            elif pygame.Rect.collidepoint(connect4_button, mouse):
                print("Load Connect 4")
                connect4.entrypoint() # pass control of the window to the connect4 module
    
    window_width, window_height = pygame.display.get_window_size()
    if window_width != menu_screen_width or window_height != menu_screen_height:
        screen = pygame.display.set_mode((menu_screen_width, menu_screen_height), pygame.RESIZABLE)
    
    screen.fill((0, 0, 0))
    screen.blit(chess_icon, chess_button)
    screen.blit(checkers_icon, checkers_button)
    screen.blit(connect4_icon, connect4_button)
    
    pygame.display.flip()
    frm.tick(30)