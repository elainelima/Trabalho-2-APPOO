import pygame

def draw_stylized_button(surface, rect, text, font, mouse_pos, is_hovered_color=(50, 200, 50), base_color=(34, 139, 34)):
    pygame.draw.rect(surface, (0, 0, 0), rect.move(3, 3), border_radius=12)
    color = is_hovered_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def draw_victory_screen(screen, width, height, font, button_font):
    screen.fill((34, 139, 34))
    title = font.render("Vitória!", True, (255, 255, 255))
    screen.blit(title, (width // 2 - title.get_width() // 2, 120))

    # Botão Jogar Novamente
    again_rect = pygame.Rect(width // 2 - 120, height // 2, 240, 60)
    pygame.draw.rect(screen, (50, 205, 50), again_rect)
    again_text = button_font.render("Jogar Novamente", True, (255, 255, 255))
    screen.blit(again_text, (again_rect.x + 20, again_rect.y + 15))

    # Botão Ranking
    ranking_rect = pygame.Rect(width // 2 - 120, height // 2 + 80, 240, 60)
    pygame.draw.rect(screen, (70, 130, 180), ranking_rect)
    ranking_text = button_font.render("Ranking", True, (255, 255, 255))
    screen.blit(ranking_text, (ranking_rect.x + 65, ranking_rect.y + 15))

    return {"jogar_novamente": again_rect, "ranking": ranking_rect}