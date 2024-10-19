import cairo

from draw_house_utils import draw_house


def main():
    width, height = 1000, 600
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    # Set the background color to white
    context.set_source_rgb(1, 1, 1)
    context.paint()

    draw_house(context, surface, width=800, height=600)
