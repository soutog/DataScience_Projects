from PIL import Image, ImageFilter

img =  Image.open('./astro.jpg')

img.thumbnail((400, 400)) # keep the aspect ratio
img.save("astro_new.png", "png")

print(img.size)