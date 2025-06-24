import pygame

def draw_stylized_button(surface, rect, text, font, mouse_pos, is_hovered_color=(50, 200, 50), base_color=(34, 139, 34)):
    pygame.draw.rect(surface, (0, 0, 0), rect.move(3, 3), border_radius=12)
    color = is_hovered_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)


# ui/screens/ranking_screen.py

import pygame

def draw_ranking_screen(screen, width, height, title_font, text_font, ranking_service, top_n=5):
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(220)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    title = title_font.render("Ranking - Modo Sem Fim", True, (255, 255, 255))
    screen.blit(title, (width // 2 - title.get_width() // 2, 60))

    top_scores = ranking_service.get_top_scores(top_n)
    for i, (_, nick, score, _) in enumerate(top_scores):
        rank_text = f"{i + 1}. {nick} - {score} pts"
        text_surface = text_font.render(rank_text, True, (255, 255, 0))
        screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, 150 + i * 40))


    # Botões
    button_width = 250
    button_height = 50
    spacing = 20
    center_x = width // 2

    back_button = pygame.Rect(center_x - button_width // 2, height - 140, button_width, button_height)
    retry_button = pygame.Rect(center_x - button_width // 2, height - 70, button_width, button_height)

    pygame.draw.rect(screen, (70, 130, 180), back_button, border_radius=10)
    pygame.draw.rect(screen, (34, 139, 34), retry_button, border_radius=10)

    back_text = text_font.render("Voltar ao Menu", True, (255, 255, 255))
    retry_text = text_font.render("Jogar Novamente", True, (255, 255, 255))

    screen.blit(back_text, (back_button.centerx - back_text.get_width() // 2, back_button.y + 10))
    screen.blit(retry_text, (retry_button.centerx - retry_text.get_width() // 2, retry_button.y + 10))

    return {"menu": back_button, "retry": retry_button}
