from PIL import Image, ImageDraw


images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

# for i in range(0, 2):
#     im = Image.new('RGBA', (width, width), color_1)
#     print(i)
#     draw = ImageDraw.Draw(im)
#     draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
#     images.append(im)
images.append(Image.open(
        'config/layer_images/0.png'))
images.append(Image.open(
        'config/layer_images/1.png'))

images[0].save('assets/d.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=1, loop=0)