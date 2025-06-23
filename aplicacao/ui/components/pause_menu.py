import pygame

def draw_pause_menu(screen, width, height, font, button_font):
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    title = font.render("Jogo Pausado", True, (255, 255, 255))
    screen.blit(title, (width // 2 - title.get_width() // 2, height // 2 - 150))

    buttons = {
        "continuar": pygame.Rect(width // 2 - 150, height // 2 - 50, 300, 60),
        "sair": pygame.Rect(width // 2 - 150, height // 2 + 30, 300, 60)
    }

    mouse_pos = pygame.mouse.get_pos()
    for label, rect in buttons.items():
        text = "Continuar" if label == "continuar" else "Sair para Menu"
        draw_button(screen, rect, text, button_font, mouse_pos)

    return buttons

def draw_button(surface, rect, text, font, mouse_pos, hover_color=(70, 130, 180), base_color=(100, 100, 100)):
    pygame.draw.rect(surface, (0, 0, 0), rect.move(3, 3), border_radius=12)
    color = hover_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)
