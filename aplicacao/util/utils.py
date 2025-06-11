
from settings import TILE_SIZE

def grid_to_pixel(grid_pos):
    """Converte (row, col) para posição central em pixels (x, y)"""
    row, col = grid_pos
    x = col * TILE_SIZE + TILE_SIZE // 2
    y = row * TILE_SIZE + TILE_SIZE // 2
    return (x, y)

def pixel_to_grid(pixel_pos):
    """Converte (x, y) em pixels para (row, col) da grade"""
    x, y = pixel_pos
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    return (row, col)
