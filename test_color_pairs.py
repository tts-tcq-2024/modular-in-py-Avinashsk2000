from color_pair import get_color_from_pair_number, get_pair_number_from_color, print_reference_manual
from color_data import MAJOR_COLORS, MINOR_COLORS
import io, sys

def test_number_to_pair():
    for pair_number in range(1, 26):
        assert get_color_from_pair_number(pair_number) == get_color_from_pair_number(pair_number)

def test_pair_to_number():
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            assert get_pair_number_from_color(major_color, minor_color) == \
                   get_pair_number_from_color(major_color, minor_color)

def test_reference_manual_output():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print_reference_manual()
    sys.stdout = sys.__stdout__
    expected_output = '\n'.join([f'{pair_number}: {get_color_from_pair_number(pair_number)[0]} {get_color_from_pair_number(pair_number)[1]}' 
                                 for pair_number in range(1, 26)]) + '\n'
    assert captured_output.getvalue() == expected_output

def run_tests():
    test_number_to_pair()
    test_pair_to_number()
    test_reference_manual_output()
    print("Done:)")

if __name__ == '__main__':
    run_tests()
