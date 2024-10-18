import cairo
import os

# Define the output directory
OUTPUT_DIR = "output_directory/"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure the output directory exists

# Function to create a surface with a background color
def create_surface(width, height):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(1, 1, 1)  # White background
    context.paint()  # Fill the background
    return surface, context

# Function to draw a rectangle
def draw_rectangle(context, x, y, rect_width, rect_height, color=(0, 0, 0)):
    context.set_line_width(2)
    context.set_source_rgb(*color)
    context.rectangle(x, y, rect_width, rect_height)
    context.stroke()

# Function to draw multiple rectangles on an expanded canvas
def windows(output_filename):
    # Create a surface with enough width for both drawings
    surface, context = create_surface(500, 200)  # 500 width, 200 height

    # Draw the first set of rectangles (regular size)
    draw_rectangle(context, 50, 150, 200, 20)  # Outer rectangle
    draw_rectangle(context, 70, 50, 160, 100)  # Inner rectangle

    # Draw the second set of rectangles (smaller size), shifted to the right
    draw_rectangle(context, 300, 70, 100, 10, (0, 0, 0))  # Smaller outer rectangle (blue)
    draw_rectangle(context, 320, 30, 60, 40, (0, 0, 0))   # Smaller inner rectangle (green)

    draw_rectangle(context, 350, 90, 60, 60, (0, 0, 0))

    # Save the result as a PNG file
    surface.write_to_png(os.path.join(OUTPUT_DIR, output_filename))
    print(f"Image saved as {output_filename}")

# Generate the combined image
windows("combined_drawing.png")
