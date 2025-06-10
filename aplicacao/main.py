import pygame
from core.game_manager import GameManager  # ou game, se for o nome do arquivo

def main():
    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Protect The Land")
    clock = pygame.time.Clock()
    FPS = 60

    game = GameManager(screen)  # Cria o gerenciador do jogo

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # Delta time em segundos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)  # Passa o evento para o game manager tratar

        game.update(dt)  # Atualiza lógica do jogo
        game.draw()      # Desenha tudo na tela
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
