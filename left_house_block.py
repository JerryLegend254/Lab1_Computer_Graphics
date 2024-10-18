import cairo 

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

#Subpath for the house (Right)rectangle
def create_left_house_block(context:cairo.Context):
    ctx.move_to(400,300)
    ctx.line_to(850,300)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(850,300)
    ctx.line_to(850,600)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(850,600)
    ctx.line_to(400,600)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(850,600)
    ctx.line_to(400,600)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    
    '''ctx.move_to(400,600)
    ctx.line_to(400,300)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)'''

    #Quadrilateral roof for (left house) section
    ctx.move_to(410,300)
    ctx.line_to(900,300)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(900,300)
    ctx.line_to(750,150)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.move_to(750,150)
    ctx.line_to(300,150)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)


    ctx.set_source_rgb(0,0,0)
    ctx.set_line_width(5)
    ctx.stroke()
