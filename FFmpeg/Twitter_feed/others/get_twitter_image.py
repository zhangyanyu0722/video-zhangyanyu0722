from PIL import Image, ImageDraw, ImageFont
import os

filename = "img01.png"
twitter = "A British Airways flight has broken the record for the\n fastest-ever subsonic flight between New York and \nLondon, reaching a top speed of more than 800mph"
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
image = Image.open("1.png")
draw = ImageDraw.Draw(image)
draw.text((100,200), twitter, font=fnt, fill= "black")
image.save(filename)
