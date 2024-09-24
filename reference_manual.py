from color_pair import get_color_from_pair_number, color_pair_to_string

def generate_reference_manual():
    manual = []
    for pair_number in range(1, 26):
        major, minor = get_color_from_pair_number(pair_number)
        manual.append(f'{pair_number}: {color_pair_to_string(major, minor)}')
    return "\n".join(manual)

def print_reference_manual():
    print(generate_reference_manual())
