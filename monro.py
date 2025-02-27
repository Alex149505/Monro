from PIL import Image
image = Image.open("monro.jpg")
red, green, blue = image.split()
div_tuple = image.split()
red = (div_tuple[0])
green = (div_tuple[1])
blue = (div_tuple[2])
(red, green, blue) = image.split()

image = red
coordinates = (50, 0, image.width, image.height)
cropped_red_left = image.crop(coordinates) 

coordinates = (25, 0, 671, 522)
cropped_red_middle = image.crop(coordinates) 

image1 = cropped_red_left
image2 = cropped_red_middle
red_blended = (image1, image2)
red_blended = Image.blend(image1, image2, 0.5)

image = blue
coordinates = (0, 0, 646, 522)
cropped_blue_right = image.crop(coordinates)

coordinates = (25, 0, 671, 522)
cropped_blue_middle = image.crop(coordinates)

image1 = cropped_blue_right
image2 = cropped_blue_middle
blue_blended = (image1, image2)
blue_blended = Image.blend(image1, image2, 0.5)

image = green
coordinates = (25, 0, 671, 522)
cropped_green = image.crop(coordinates)

red =  red_blended
green = cropped_green
blue = blue_blended
image_final = (red, green, blue)
image_final = Image.merge("RGB", (red, green, blue))
image_final.save("monro_final.jpg")

image = image_final
image.thumbnail((80, 80))  
image.save("monro_final_80.jpg")









