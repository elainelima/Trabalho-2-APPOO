


import pygame

def draw_stylized_button(surface, rect, text, font, mouse_pos,
                         is_hovered_color=(72, 61, 139), base_color=(123, 104, 238)):
    shadow_offset = 4
    shadow_rect = rect.move(shadow_offset, shadow_offset)
    pygame.draw.rect(surface, (30, 30, 30), shadow_rect, border_radius=12)

    color = is_hovered_color if rect.collidepoint(mouse_pos) else base_color
    pygame.draw.rect(surface, color, rect, border_radius=12)

    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def draw_victory_screen(screen, width, height, button_font):
    # Fundo azul escuro
    screen.fill((18, 32, 47))

    # Fonte estilizada para título (Arial Black)
    title_font = pygame.font.SysFont("arialblack", 72, bold=True)
    title_text = "Vitória!"

    # Renderiza texto
    title_surface = title_font.render(title_text, True, (255, 215, 0))  # ouro

    spacing = 15
    trophy_size = 48  # tamanho do ícone

    # Carrega o ícone dentro da função 
    TROFEU_PATH = "assets/icons/trofeu.png"
    trofeu_icon = pygame.image.load(TROFEU_PATH).convert_alpha()
    trofeu_icon = pygame.transform.smoothscale(trofeu_icon, (trophy_size, trophy_size))

    total_width = title_surface.get_width() + spacing + trophy_size
    x_start = width // 2 - total_width // 2
    y_pos = 100

    # Alinha verticalmente o texto ao centro do ícone
    text_y = y_pos + (trophy_size - title_surface.get_height()) // 2

    # Desenha texto e ícone
    screen.blit(title_surface, (x_start, text_y))
    screen.blit(trofeu_icon, (x_start + title_surface.get_width() + spacing, y_pos))

    mouse_pos = pygame.mouse.get_pos()

    # Botão Jogar Novamente
    again_rect = pygame.Rect(width // 2 - 140, height // 2, 280, 60)
    draw_stylized_button(screen, again_rect, "Jogar Novamente", button_font, mouse_pos,
                         is_hovered_color=(255, 140, 0), base_color=(255, 165, 0))

    # Botão Voltar ao Menu
    menu_rect = pygame.Rect(width // 2 - 140, height // 2 + 90, 280, 60)
    draw_stylized_button(screen, menu_rect, "Voltar ao Menu", button_font, mouse_pos,
                         is_hovered_color=(70, 130, 180), base_color=(65, 105, 225))

    return {"retry": again_rect, "menu": menu_rect}

