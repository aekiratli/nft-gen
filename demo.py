from PIL import Image

images = [Image.open(x) for x in ['./config/layer_images/idle/s1/layer1/1.png',
                                  './config/layer_images/idle/s2/layer1/1.png',
                                  './config/layer_images/right/s1/layer1/1.png',
                                  './config/layer_images/right/s2/layer1/1.png']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_im.save('test2.png')


im1 = Image.open('test.png')
im2 = Image.open('test2.png')
def get_concat_v(im1, im2):
    dst = Image.new('RGBA', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst
get_concat_v(im1, im1).save('test3.png')
