import pygame
from core.game_manager import GameManager  

def main():
    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Protect The Land")
    clock = pygame.time.Clock()
    FPS = 60

    game = GameManager(screen)
    font = pygame.font.SysFont(None, 60)
    button_font = pygame.font.SysFont(None, 40)
    game_over = False

    while True:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mx, my):
                        # Reinicia o jogo
                        game = GameManager(screen)
                        game_over = False
            else:
                game.handle_event(event)

        if not game_over:
            game.update(dt)
            if game.base_hp <= 0:
                game_over = True

        game.draw()

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            text = font.render("Game Over", True, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100))

            button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 60)
            mouse_pos = pygame.mouse.get_pos()
            draw_stylized_button(screen, button_rect, "Jogar Novamente", button_font, mouse_pos)

        pygame.display.flip()

def draw_stylized_button(surface, rect, text, font, mouse_pos, is_hovered_color=(50, 200, 50), base_color=(34, 139, 34)):
    pygame.draw.rect(surface, (0, 0, 0), rect.move(3, 3), border_radius=12)  
    color = is_hovered_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

if __name__ == "__main__":
    main()
