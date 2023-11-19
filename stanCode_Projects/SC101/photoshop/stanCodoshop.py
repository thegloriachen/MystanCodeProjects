"""
File: stanCodoshop.py
Name: Gloria
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    input_pixel = pixel
    get_pixel_red = input_pixel.red
    get_pixel_green = input_pixel.green
    get_pixel_blue = input_pixel.blue
    red_pixel_avg = red
    green_pixel_avg = green
    blue_pixel_avg = blue
    # calculate the color distance
    color_dist = math.sqrt((red_pixel_avg-get_pixel_red)**2 + (green_pixel_avg-get_pixel_green)**2 +
                           (blue_pixel_avg-get_pixel_blue)**2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    pixel_list = pixels
    total_pixel_red = 0
    total_pixel_green = 0
    total_pixel_blue = 0
    count = 0
    # for each loop to get RGB values from every pixel
    for pixel in pixel_list:
        one_pixel = pixel
        total_pixel_red += one_pixel.red
        total_pixel_green += one_pixel.green
        total_pixel_blue += one_pixel.blue
        count += 1
    # calculate the average RGB values
    avg_red = int(total_pixel_red/count)
    avg_green = int(total_pixel_green/count)
    avg_blue = int(total_pixel_blue/count)
    rgb = [avg_red, avg_green, avg_blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    pixel_list = pixels
    avg_rgb = get_average(pixel_list)
    avg_red = avg_rgb[0]
    avg_green = avg_rgb[1]
    avg_blue = avg_rgb[2]
    # Pixel is an object, so the initialization for best_pixel should be None
    best_pixel = None
    min_color_dist = 999
    for pixel in pixel_list:
        one_pixel = pixel
        get_color_dist = get_pixel_dist(one_pixel, avg_red, avg_green, avg_blue)
        if get_color_dist <= min_color_dist:
            min_color_dist = get_color_dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    image_list = images
    pixel_compare_list = []
    # for loop: to find the best pixel from the list of images, and replace the pixel from blank image.
    for x in range(width):
        for y in range(height):
            for image in image_list:
                one_image = image
                get_pixel_from_image = SimpleImage.get_pixel(one_image, x, y)
                pixel_compare_list.append(get_pixel_from_image)
            best_pixel = get_best_pixel(pixel_compare_list)
            # replace the pixel from blank image.
            result_pixel = SimpleImage.get_pixel(result, x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
            pixel_compare_list = []
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
