# %% pyramid_of_cubes_bricks_rounded

## Dependencies

import pygame
import subprocess as sp

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1024, 756  # 1k

# Define cube dimensions
cube_width = 60
cube_height = 45
cube_spacing = 12

# Define pyramid dimensions
pyramid_size = 25

# Define colors
category1 = "#3182bd"
category2 = "#fdae6b"
category3 = "#e6550d"

# Define color percentages
category1_percentage = 5
category2_percentage = 20

def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_upside_down_pyramid(category_order):
    total_cubes = sum(range(pyramid_size + 1))
    category1_cubes = int(category1_percentage / 100 * total_cubes)
    category2_cubes = int(category2_percentage / 100 * total_cubes)

    # Increase DPI by setting a larger surface size
    dpi_factor = 2  # Increase this factor to increase DPI
    pyramid_surface = pygame.Surface((width * dpi_factor, height * dpi_factor), pygame.SRCALPHA)
    current_cube = 0
    for i in range(pyramid_size):
        start_x = (width * dpi_factor - i * (cube_width + cube_spacing)) / 2
        for j in range(i+1):
            x = start_x + j * (cube_width + cube_spacing)
            y = height * dpi_factor - (pyramid_size - i) * (cube_height + cube_spacing)

            if current_cube < category1_cubes:
                draw_rounded_rect(pyramid_surface, category_order[0], (x, y, cube_width, cube_height), 5)  # Category 1
            elif current_cube < category1_cubes + category2_cubes:
                draw_rounded_rect(pyramid_surface, category_order[1], (x, y, cube_width, cube_height), 5)  # Category 2
            else:
                draw_rounded_rect(pyramid_surface, category_order[2], (x, y, cube_width, cube_height), 5)  # Category 3

            current_cube += 1

    return pyramid_surface

# Main loop
# Example of custom category order
custom_category_order = [category1, category2, category3]
pyramid = draw_upside_down_pyramid(custom_category_order)  # Draw the pyramid once

#path_adj = 'explorer '+'"'+'bespoke_pyramid_of_cubes_bricks_rounded.png'+'"'

chart_out = _vl + r'\bespoke\bespoke_pyramid_of_cubes_bricks_rounded.png'

# Save the frame as a PNG file with higher DPI
pygame.image.save(pyramid, chart_out)
#sp.Popen(path_adj)
sp.Popen(chart_out, shell=True) #open file

#exec(open(_vl+r'\bespoke\bespoke_pyramid_of_cubes_bricks_rounded.py').read())
