import cairo
import math

# Set up the surface and context
WIDTH, HEIGHT = 200, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Set background color
ctx.set_source_rgb(1, 1, 1)  # White background
ctx.paint()

# Draw the full moon (outer circle)
ctx.arc(100, 100, 50, 0, 2 * math.pi)  # (x, y, radius, start angle, end angle)
ctx.set_source_rgb(0.9, 0.9, 0.9)  # Light gray for moon
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)  # Black outline for moon
ctx.stroke()

# Draw the shadow (inner circle creating the crescent effect)
ctx.arc(70, 100, 50, 0, 2 * math.pi)  # (x, y, radius, start angle, end angle)
ctx.set_source_rgb(1, 1, 1)  # White to create the shadow part of the crescent
ctx.fill()

# Add outline to the crescent
ctx.arc(100, 100, 50, 0, 2 * math.pi)  # (x, y, radius, start angle, end angle)
ctx.set_source_rgb(0, 0, 0)  # Black outline for the crescent moon
ctx.set_line_width(2)
ctx.stroke()

# Save the drawing
surface.write_to_png("moon1.png")
