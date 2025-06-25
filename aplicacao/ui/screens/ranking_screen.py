import pygame

def draw_ranking_screen(screen, width, height, title_font, text_font, ranking_service, map, top_n=5):
    # Fundo escurecido
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(220)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    # Box de ranking
    box_width, box_height = 500, 350
    box_x = width // 2 - box_width // 2
    box_y = 100
    pygame.draw.rect(screen, (30, 30, 30), (box_x, box_y, box_width, box_height), border_radius=12)
    pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, box_width, box_height), 2, border_radius=12)

    # Título
    title = title_font.render("Ranking - Modo Sem Fim", True, (255, 255, 255))
    screen.blit(title, (width // 2 - title.get_width() // 2, box_y - 60))

    # Carrega estrela
    STAR_PATH = "assets/icons/star.png"
    star_icon = pygame.image.load(STAR_PATH).convert_alpha()
    star_icon = pygame.transform.scale(star_icon, (36, 36))

    # Listagem
    top_scores = ranking_service.get_top_scores(top_n, map)
    for i, (_, nick, score, _) in enumerate(top_scores):
        y = box_y + 40 + i * 50

        if i == 0:
            # Primeira posição com estrela e destaque
            score_text = f"{nick} - {score} pts"
            text_surface = text_font.render(score_text, True, (255, 215, 0))
            text_x = width // 2 - text_surface.get_width() // 2 + 20
            screen.blit(star_icon, (text_x - 45, y - 4))
            screen.blit(text_surface, (text_x, y))
        else:
            rank_text = f"{i + 1}. {nick} - {score} pts"
            text_surface = text_font.render(rank_text, True, (255, 255, 0))
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, y))

    # Botões
    button_width, button_height = 250, 40
    center_x = width // 2

    back_button = pygame.Rect(center_x - button_width // 2, height - 120, button_width, button_height)
    retry_button = pygame.Rect(center_x - button_width // 2, height - 60, button_width, button_height)

    mouse_pos = pygame.mouse.get_pos()
    draw_stylized_button(screen, back_button, "Voltar ao Menu", text_font, mouse_pos)
    draw_stylized_button(screen, retry_button, "Jogar Novamente", text_font, mouse_pos)

    return {"menu": back_button, "retry": retry_button}

# Botão com sombra e hover
def draw_stylized_button(surface, rect, text, font, mouse_pos, hover_color=(60, 160, 60), base_color=(40, 120, 40)):
    shadow_rect = rect.move(3, 3)
    pygame.draw.rect(surface, (0, 0, 0), shadow_rect, border_radius=12)

    is_hovered = rect.collidepoint(mouse_pos)
    color = hover_color if is_hovered else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, text_surface.get_rect(center=rect.center))