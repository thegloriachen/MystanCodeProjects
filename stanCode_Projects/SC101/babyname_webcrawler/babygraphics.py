"""
File: babygraphics.py
Name: Gloria
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    interval = (width-GRAPH_MARGIN_SIZE*2) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + interval*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # draw the fixed edge lines of the window
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # draw the vertical lines associated with the current year.
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, font=10)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    y_interval = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2) / 1000
    color_index = 0
    for name in lookup_names:
        for key, value in name_data.items():
            if name == key:
                data = value
                rank_in_data_sorted = sorted(data)          # in order to loop over the data by sorted years.
                for key1, value1 in data.items():
                    for i in range(len(YEARS)-1):
                        year1 = YEARS[i]
                        year_index1 = i
                        year2 = YEARS[i+1]
                        year_index2 = i+1
                        if str(year1) in rank_in_data_sorted:
                            if str(year2) in rank_in_data_sorted:
                                # get rank of the first point.
                                rank1 = data[str(year1)]
                                # get x, y position of the second point.
                                first_x_position = get_x_coordinate(CANVAS_WIDTH, year_index1)
                                first_y_position = GRAPH_MARGIN_SIZE + (y_interval * int(rank1))
                                canvas.create_text(first_x_position + LINE_WIDTH, first_y_position,
                                                   text=name + " " + rank1, anchor=tkinter.SW, font=10,
                                                   fill=COLORS[color_index])
                                # get rank of the second point
                                rank2 = data[str(year2)]
                                # get x, y position of the second point.
                                second_x_position = get_x_coordinate(CANVAS_WIDTH, year_index2)
                                second_y_position = GRAPH_MARGIN_SIZE + (y_interval * int(rank2))
                                canvas.create_text(second_x_position + LINE_WIDTH, second_y_position,
                                                   text=name + " " + rank2, anchor=tkinter.SW, font=10,
                                                   fill=COLORS[color_index])
                            else:
                                # get rank for the first point.
                                rank1 = data[str(year1)]
                                # get x, y position of the first point.
                                first_x_position = get_x_coordinate(CANVAS_WIDTH, year_index1)
                                first_y_position = GRAPH_MARGIN_SIZE + (y_interval * int(rank1))
                                canvas.create_text(first_x_position + LINE_WIDTH, first_y_position,
                                                   text=name + " " + rank1, anchor=tkinter.SW, font=10,
                                                   fill=COLORS[color_index])
                                # get x, y position of the second point.
                                second_x_position = get_x_coordinate(CANVAS_WIDTH, year_index2)
                                second_y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                                canvas.create_text(second_x_position + LINE_WIDTH, second_y_position, text=name + " *",
                                                   anchor=tkinter.SW, font=10, fill=COLORS[color_index])
                        else:
                            if str(year2) in rank_in_data_sorted:
                                # get x, y position of the first point.
                                first_x_position = get_x_coordinate(CANVAS_WIDTH, year_index1)
                                first_y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                                canvas.create_text(first_x_position + LINE_WIDTH, first_y_position, text=name + " *",
                                                   anchor=tkinter.SW, font=10, fill=COLORS[color_index])
                                # get rank of the second point.
                                rank2 = data[str(year2)]
                                # get x, y position of the second point.
                                second_x_position = get_x_coordinate(CANVAS_WIDTH, year_index2)
                                second_y_position = GRAPH_MARGIN_SIZE + (y_interval * int(rank2))
                                canvas.create_text(second_x_position + LINE_WIDTH, second_y_position,
                                                   text=name + " " + rank2, anchor=tkinter.SW, font=10,
                                                   fill=COLORS[color_index])
                            else:
                                # get x, y position of the first point.
                                first_x_position = get_x_coordinate(CANVAS_WIDTH, year_index1)
                                first_y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                                canvas.create_text(first_x_position + LINE_WIDTH, first_y_position, text=name + " *",
                                                   anchor=tkinter.SW, font=10, fill=COLORS[color_index])
                                # get x, y position of the second point.
                                second_x_position = get_x_coordinate(CANVAS_WIDTH, year_index2)
                                second_y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                                canvas.create_text(second_x_position + LINE_WIDTH, second_y_position, text=name + " *",
                                                   anchor=tkinter.SW, font=10, fill=COLORS[color_index])
                        # create the line according to the result of if statement.
                        canvas.create_line(first_x_position, first_y_position, second_x_position,
                                           second_y_position, width=LINE_WIDTH, fill=COLORS[color_index])
        # set up the color for the next lookup name.
        if color_index != 3:
            color_index += 1
        else:
            color_index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
