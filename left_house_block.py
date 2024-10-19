import cairo
from utils import fractionize


# Subpath for the house (Right)rectangle
def create_left_house_block(ctx: cairo.Context, x=800, y=600):
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
