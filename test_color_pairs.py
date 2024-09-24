from color_pair import get_color_from_pair_number, get_pair_number_from_color
from color_data import MAJOR_COLORS, MINOR_COLORS

def test_number_to_pair():
    """Tests number to color pair mapping."""
    for i in range(1, 26):
        assert get_color_from_pair_number(i) == get_color_from_pair_number(i)

def test_pair_to_number():
    """Tests color pair to number mapping."""
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            expected_pair_number = get_pair_number_from_color(major_color, minor_color)
            assert expected_pair_number == get_pair_number_from_color(major_color, minor_color)

def run_tests():
    """Runs all test cases."""
    test_number_to_pair()
    test_pair_to_number()
    print('All tests passed!')

if __name__ == '__main__':
    run_tests()
