"""
File: blur.py
Name: Gloria
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, blurred image.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x+1, y)
                new_img_pixel3 = img.get_pixel(x, y+1)
                new_img_pixel4 = img.get_pixel(x+1, y+1)
                avg_red = (new_img_pixel1.red+new_img_pixel2.red+new_img_pixel3.red+new_img_pixel4.red) // 4
                avg_green = (new_img_pixel1.green+new_img_pixel2.green+new_img_pixel3.green+new_img_pixel4.green) // 4
                avg_blue = (new_img_pixel1.blue+new_img_pixel2.blue+new_img_pixel3.blue+new_img_pixel4.blue) // 4
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(img.width-1, y)
                new_img_pixel2 = img.get_pixel(img.width-2, y)
                new_img_pixel3 = img.get_pixel(img.width-1, y+1)
                new_img_pixel4 = img.get_pixel(img.width-2, y+1)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red) // 4
                avg_green = (new_img_pixel1.green + new_img_pixel2.green + new_img_pixel3.green + new_img_pixel4.green) // 4
                avg_blue = (new_img_pixel1.blue + new_img_pixel2.blue + new_img_pixel3.blue + new_img_pixel4.blue) // 4
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, img.height-1)
                new_img_pixel2 = img.get_pixel(x, img.height-2)
                new_img_pixel3 = img.get_pixel(x+1, img.height-1)
                new_img_pixel4 = img.get_pixel(x+1, img.height-2)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red) // 4
                avg_green = (new_img_pixel1.green + new_img_pixel2.green + new_img_pixel3.green + new_img_pixel4.green) // 4
                avg_blue = (new_img_pixel1.blue + new_img_pixel2.blue + new_img_pixel3.blue + new_img_pixel4.blue) // 4
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(img.width-1, img.height-1)
                new_img_pixel2 = img.get_pixel(img.width-1, img.height-2)
                new_img_pixel3 = img.get_pixel(img.width-2, img.height-1)
                new_img_pixel4 = img.get_pixel(img.width-2, img.height-2)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red) // 4
                avg_green = (new_img_pixel1.green + new_img_pixel2.green + new_img_pixel3.green + new_img_pixel4.green) // 4
                avg_blue = (new_img_pixel1.blue + new_img_pixel2.blue + new_img_pixel3.blue + new_img_pixel4.blue) // 4
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x-1, y)
                new_img_pixel3 = img.get_pixel(x+1, y)
                new_img_pixel4 = img.get_pixel(x, y+1)
                new_img_pixel5 = img.get_pixel(x-1, y+1)
                new_img_pixel6 = img.get_pixel(x+1, y+1)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red) // 4
                avg_green = (new_img_pixel1.green + new_img_pixel2.green + new_img_pixel3.green + new_img_pixel4.green) // 4
                avg_blue = (new_img_pixel1.blue + new_img_pixel2.blue + new_img_pixel3.blue + new_img_pixel4.blue) // 4
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x-1, y)
                new_img_pixel3 = img.get_pixel(x+1, y)
                new_img_pixel4 = img.get_pixel(x, y-1)
                new_img_pixel5 = img.get_pixel(x-1, y-1)
                new_img_pixel6 = img.get_pixel(x+1, y-1)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.red + new_img_pixel6.red) // 6
                avg_green = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.green + new_img_pixel6.green) // 6
                avg_blue = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.blue + new_img_pixel6.blue) // 6
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x, y-1)
                new_img_pixel3 = img.get_pixel(x, y+1)
                new_img_pixel4 = img.get_pixel(x+1, y-1)
                new_img_pixel5 = img.get_pixel(x+1, y+1)
                new_img_pixel6 = img.get_pixel(x+1, y)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.red + new_img_pixel6.red) // 6
                avg_green = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                             + new_img_pixel5.green + new_img_pixel6.green) // 6
                avg_blue = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                            + new_img_pixel5.blue + new_img_pixel6.blue) // 6
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x, y-1)
                new_img_pixel3 = img.get_pixel(x, y+1)
                new_img_pixel4 = img.get_pixel(x-1, y - 1)
                new_img_pixel5 = img.get_pixel(x-1, y + 1)
                new_img_pixel6 = img.get_pixel(x-1, y)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.red + new_img_pixel6.red) // 6
                avg_green = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                             + new_img_pixel5.green + new_img_pixel6.green) // 6
                avg_blue = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                            + new_img_pixel5.blue + new_img_pixel6.blue) // 6
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
            else:
                # Inner pixels.
                new_img_pixel = new_img.get_pixel(x, y)
                new_img_pixel1 = img.get_pixel(x, y)
                new_img_pixel2 = img.get_pixel(x, y-1)
                new_img_pixel3 = img.get_pixel(x, y+1)
                new_img_pixel4 = img.get_pixel(x-1, y-1)
                new_img_pixel5 = img.get_pixel(x-1, y+1)
                new_img_pixel6 = img.get_pixel(x-1, y)
                new_img_pixel7 = img.get_pixel(x+1, y-1)
                new_img_pixel8 = img.get_pixel(x+1, y+1)
                new_img_pixel9 = img.get_pixel(x+1, y)
                avg_red = (new_img_pixel1.red + new_img_pixel2.red + new_img_pixel3.red + new_img_pixel4.red
                           + new_img_pixel5.red + new_img_pixel6.red + new_img_pixel7.red + new_img_pixel8.red
                           + new_img_pixel9.red) // 9
                avg_green = (new_img_pixel1.green + new_img_pixel2.green + new_img_pixel3.green + new_img_pixel4.green
                           + new_img_pixel5.green + new_img_pixel6.green + new_img_pixel7.green + new_img_pixel8.green
                           + new_img_pixel9.green) // 9
                avg_blue = (new_img_pixel1.blue + new_img_pixel2.blue + new_img_pixel3.blue + new_img_pixel4.blue
                            + new_img_pixel5.blue + new_img_pixel6.blue + new_img_pixel7.blue + new_img_pixel8.blue
                            + new_img_pixel9.blue) // 9
                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue
    return new_img


def main():
    """
    This file shows the original image(smiley-face.png) first, and then its blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
