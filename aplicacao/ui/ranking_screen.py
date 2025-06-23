import pygame

def draw_ranking_screen(screen, width, height, font, button_font, rankings):
    screen.fill((30, 30, 30))
    title = font.render("Ranking", True, (255, 215, 0))
    screen.blit(title, (width // 2 - title.get_width() // 2, 60))

    # Exibe os rankings (nome, score)
    y = 160
    for i, (name, score) in enumerate(rankings[:10], 1):
        text = button_font.render(f"{i}. {name} - {score}", True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, y))
        y += 40

    # Botão de voltar
    back_rect = pygame.Rect(width // 2 - 100, height - 120, 200, 50)
    pygame.draw.rect(screen, (70, 130, 180), back_rect)
    back_text = button_font.render("Voltar", True, (255, 255, 255))
    screen.blit(back_text, (back_rect.x + 50, back_rect.y + 10))

    return {"voltar": back_rect}