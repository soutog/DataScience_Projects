from PIL import Image, ImageFilter

img =  Image.open('./Pokedex/pikachu.jpg')
# print(img)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur_pikachu.png", 'png')

converted_img = img.convert("L")
converted_img.save("grey_pikachu.png", "png")

# converted_img.show()

crooked = converted_img.rotate(90)
crooked.save("crooked_pikachu.png", "png")

resize = converted_img.resize((40, 30))
resize.save("resized_pikachu.png", "png")

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped_pikachu.png", "png")
