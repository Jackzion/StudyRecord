from PIL import Image , ImageFilter , ImageDraw , ImageFont

im = Image.open('./image/wallhaven-z8e8qy.jpg')
w , h = im.size
print('size : %s * %s' % (w,h))
im.thumbnail((w/2,h/2))
print('size : %s * %s' % (w/2,h/2))
im.save('./image/thumbnail.jpg','jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('./image/blur.jpg','jpeg')

# 验证码生成
import random

def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# font
font = ImageFont.truetype('cmb10.ttf' , 36)
# init draw
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
# output
for t in range(4):
    draw.text((60*t + 10,10),rndChar(),font=font,fill=rndColor2())

# blur
image = image.filter(ImageFilter.BLUR)
image.save('./image/code.jpg', 'jpeg')