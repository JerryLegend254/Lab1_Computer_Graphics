import cairo
import left_house_block

import main_block
if __name__ == "__main__":
    print("Hello, World!")
    width, height = 1200, 1000
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    # Set the background color to white
    context.set_source_rgb(1, 1, 1)
    context.paint()
    main_block.draw_left_block(context)
    left_house_block.create_left_house_block(context)

    surface.write_to_png('final.png')
