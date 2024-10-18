import cairo
import math


# Create a surface and context
def draw_roof(context):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Bottom line of the roof
    context.move_to(120, 230)
    context.line_to(150, 200)
    context.line_to(300, 50)
    context.line_to(450, 200)
    context.line_to(480, 230)
    context.stroke()

    # Top line of the roof
    context.move_to(120, 230)
    context.line_to(100, 210)
    context.line_to(300, 10)
    context.line_to(500, 215)
    context.line_to(480, 230)
    context.stroke()


# Function to draw the house body
def draw_house(context):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Left rectangular hut
    context.move_to(150, 200)
    context.line_to(150, 400)
    context.line_to(450, 400)
    context.line_to(450, 200)
    context.stroke()


# Function to draw the windows
def draw_windows(context):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Small square window
    context.rectangle(275, 150, 50, 50)  # (x, y, width, height)
    context.stroke()

    # Big rectangular window
    context.rectangle(215, 250, 170, 100)
    context.stroke()

    # Small rectangle under the big rectangular window
    context.rectangle(200, 350, 200, 10)
    context.stroke()

    context.rectangle(700, 250, 170, 100)
    context.stroke()

    context.rectangle(685, 350, 200, 10)
    context.stroke()

    context.rectangle(135, 400, 800, 30)
    context.stroke()


def draw_left_block(context):
    draw_roof(context)
    draw_house(context)
    draw_windows(context)
