from color_pair import get_color_from_pair_number, get_pair_number_from_color
def test_number_to_pair():
    """Tests number to color pair mapping."""
    for i in range(1, 26):
        assert get_color_from_pair_number(i) == get_color_from_pair_number(i)
def test_pair_to_number():
    """Tests color pair to number mapping."""
    for major_color in ['White', 'Red', 'Black', 'Yellow', 'Violet']:
        for minor_color in ["Blue", "Orange", "Green", "Brown", "Slate"]:
            assert get_pair_number_from_color(major_color, minor_color) == \
                   get_pair_number_from_color(major_color, minor_color)
def test_exceptions():
    """Tests invalid inputs."""
    for invalid_input in [26, 'Pink', 'Cyan', ('Pink', 'Cyan')]:
        try:
            if isinstance(invalid_input, int):
                get_color_from_pair_number(invalid_input)
            else:
                major, minor = invalid_input if isinstance(invalid_input, tuple) else ('White', invalid_input)
                get_pair_number_from_color(major, minor)
        except Exception:
            pass
def run_tests():
    test_number_to_pair()
    test_pair_to_number()
    test_exceptions()
    print("All tests passed!")
if __name__ == '__main__':
    run_tests()
