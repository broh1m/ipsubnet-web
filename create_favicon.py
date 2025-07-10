from PIL import Image, ImageDraw
import math

def create_favicon():
    # Create a new image with a transparent background
    size = 32
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Colors
    primary_color = (74, 144, 226)  # #4A90E2
    light_color = (74, 144, 226, 26)  # #4A90E2 with 10% opacity
    
    # Draw background circle
    draw.ellipse([1, 1, size-1, size-1], fill=light_color)
    
    # Draw network nodes
    center = size // 2
    node_radius = 2
    small_node_radius = 1.5
    
    # Center node
    draw.ellipse([center-node_radius, center-node_radius, 
                 center+node_radius, center+node_radius], 
                 fill=primary_color)
    
    # Peripheral nodes
    for angle in [0, 90, 180, 270]:
        x = center + int(8 * math.cos(math.radians(angle)))
        y = center + int(8 * math.sin(math.radians(angle)))
        draw.ellipse([x-small_node_radius, y-small_node_radius,
                     x+small_node_radius, y+small_node_radius],
                     fill=primary_color)
    
    # Draw connections
    for angle in [0, 90, 180, 270]:
        x = center + int(8 * math.cos(math.radians(angle)))
        y = center + int(8 * math.sin(math.radians(angle)))
        draw.line([center, center, x, y], fill=primary_color, width=1)
    
    # Draw diagonal connections
    for angle in [45, 135, 225, 315]:
        x = center + int(6 * math.cos(math.radians(angle)))
        y = center + int(6 * math.sin(math.radians(angle)))
        draw.line([center, center, x, y], fill=primary_color, width=1)
    
    # Save as ICO
    image.save('static/favicon.ico', format='ICO')

if __name__ == '__main__':
    create_favicon() 