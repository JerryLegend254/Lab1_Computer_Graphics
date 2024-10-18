import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


# Subpath for the house (Right)rectangle
def create_left_house_block(ctx: cairo.Context):
    ctx.move_to(480, 200)
    ctx.line_to(920, 200)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(920, 200)
    ctx.line_to(920, 400)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(920, 400)
    ctx.line_to(450, 400)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(920, 200)
    ctx.line_to(487, 200)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    '''ctx.move_to(400,600)
    ctx.line_to(400,300)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)'''

    # Quadrilateral roof for (left house) section
    ctx.move_to(487, 200)
    ctx.line_to(950, 200)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(950, 200)
    ctx.line_to(850, 10)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(300, 10)
    ctx.line_to(850, 10)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(3)
    ctx.stroke()
