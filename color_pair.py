from color_data import MAJOR_COLORS, MINOR_COLORS

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    major_index = MAJOR_COLORS.index(major_color)
    minor_index = MINOR_COLORS.index(minor_color)
    return major_index * len(MINOR_COLORS) + minor_index + 1

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'
