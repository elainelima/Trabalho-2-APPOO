import pygame

def draw_stylized_button(surface, rect, text, font, mouse_pos, is_hovered_color=(50, 200, 50), base_color=(34, 139, 34)):
    pygame.draw.rect(surface, (0, 0, 0), rect.move(3, 3), border_radius=12)
    color = is_hovered_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def draw_victory_screen(screen, width, height, font, button_font):
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(180)
    overlay.fill((255, 255, 255))
    screen.blit(overlay, (0, 0))

    text = font.render("Vitória!", True, (0, 180, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 100))

    button_rect = pygame.Rect(width // 2 - 150, height // 2, 300, 60)


    mouse_pos = pygame.mouse.get_pos()
    draw_stylized_button(screen, button_rect, "Jogar Novamente", button_font, mouse_pos)
    draw_stylized_button(screen, button_rect, "Jo")

    return button_rect