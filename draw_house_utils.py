import cairo
from utils import fractionize


# Create a surface and context
def draw_roof(context, x=800, y=600):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Bottom line of the roof
    # context.move_to(120, 230)
    # context.line_to(150, 200)
    context.move_to(fractionize(x, 0.15), fractionize(y, 0.383))
    context.line_to(fractionize(x, 0.1875), fractionize(y, 0.333))
    # context.line_to(300, 50)
    # context.line_to(450, 200)
    context.line_to(fractionize(x, 0.375), fractionize(y, 0.083))
    context.line_to(fractionize(x, 0.5625), fractionize(y, 0.333))
    # context.line_to(480, 230)
    context.line_to(fractionize(x, 0.6), fractionize(y, 0.383))
    context.stroke()

    # Top line of the roof
    # context.move_to(120, 230)
    # context.line_to(100, 210)
    # context.line_to(300, 10)
    # context.line_to(500, 215)
    # context.line_to(480, 230)
    context.move_to(fractionize(x, 0.15), fractionize(y, 0.383))
    context.line_to(fractionize(x, 0.125), fractionize(y, 0.35))
    context.line_to(fractionize(x, 0.375), fractionize(y, 0.017))
    context.line_to(fractionize(x, 0.625), fractionize(y, 0.35))
    context.line_to(fractionize(x, 0.6), fractionize(y, 0.383))
    context.stroke()


# Function to draw the house left block
def draw_left_block(context, x=800, y=600):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Left rectangular hut
    # context.move_to(150, 200)
    # context.line_to(150, 400)
    # context.line_to(450, 400)
    # context.line_to(450, 200)
    context.move_to(fractionize(x, 0.1875), fractionize(y, 0.333))
    context.line_to(fractionize(x, 0.1875), fractionize(y, 0.667))
    context.line_to(fractionize(x, 0.5625), fractionize(y, 0.667))
    context.line_to(fractionize(x, 0.5625), fractionize(y, 0.333))
    context.stroke()


# Function to draw the windows
def draw_windows(context, x=800, y=600, window_width=50, window_height=50):
    context.set_source_rgb(0, 0, 0)
    context.set_line_width(3)

    # Small square window
    context.rectangle(fractionize(x, 0.34375), fractionize(
        y, 0.25), window_width, window_height)
    context.stroke()

    # Big rectangular window
    context.rectangle(fractionize(x, 0.26875), fractionize(
        y, 0.417), window_width * 3.4, window_height * 2)
    context.stroke()

    # Small rectangle under the big rectangular window
    context.rectangle(fractionize(x, 0.25), fractionize(
        y, 0.583), window_width * 4, window_height / 5)
    context.stroke()

    context.rectangle(fractionize(x, 0.875), fractionize(
        y, 0.417), window_width * 3.4, window_height * 2)
    context.stroke()

    context.rectangle(fractionize(x, 0.85625), fractionize(
        y, 0.583), window_width * 4, window_height / 5)
    context.stroke()


# Function to draw the house base
def draw_base(context, x=800, y=600):

    # context.rectangle(135, 400, 800, 30)
    context.rectangle(fractionize(x, 0.16875), fractionize(
        y, 0.667), fractionize(x, 1), fractionize(y, 0.05))
    context.stroke()


def draw_right_block(ctx, x=800, y=600):
    ctx.move_to(fractionize(x, 1.15), fractionize(600, 0.333))
    ctx.line_to(fractionize(x, 1.15), fractionize(600, 0.667))
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    ctx.move_to(fractionize(800, 0.6105), fractionize(600, 0.333))
    ctx.line_to(fractionize(800, 1.1875), fractionize(600, 0.333))
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    ctx.move_to(fractionize(800, 1.1875), fractionize(600, 0.333))
    ctx.line_to(fractionize(800, 1.0625), fractionize(600, 0.083))
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    ctx.move_to(fractionize(800, 0.425), fractionize(600, 0.083))
    ctx.line_to(fractionize(800, 1.0625), fractionize(600, 0.083))
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(3)
    ctx.stroke()


def draw_house(context, surface, width, height, output_filename="output_dir/house.png"):
    draw_roof(context, width, height)
    draw_left_block(context, width, height)
    draw_base(context, width, height)
    draw_windows(context, width, height)
    draw_right_block(context, width, height)
    surface.write_to_png(output_filename)
