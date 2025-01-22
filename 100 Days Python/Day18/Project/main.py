###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
Color = colorgram.extract('image.jpg', 30)
for colors in Color:
    r=colors.rgb.r
    g=colors.rgb.g
    b=colors.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)