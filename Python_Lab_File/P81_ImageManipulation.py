from PIL import Image, ImageFilter

img = Image.open("fate.png")

cropped_img = img.crop((50, 50, 1000, 1000))
cropped_img.show()

resized_img = img.resize((1000, 1000))
resized_img.show()

rotated_img = img.rotate(90)
rotated_img.show()

blurred_img = img.filter(ImageFilter.GaussianBlur(55))
blurred_img.show()

img.save("fate_conv.jpg")