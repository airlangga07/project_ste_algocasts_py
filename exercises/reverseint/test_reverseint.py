from reverseint import reverseint

def test_reverseint_handles_zero_as_input():
    assert reverseint(0) == 0

def test_reverseint_flips_a_positive_number():
    assert reverseint(5) == 5
    assert reverseint(15) == 51
    assert reverseint(90) == 9
    assert reverseint(2359) == 9532

def test_reverseint_flips_a_negative_number():
    assert reverseint(-5) == -5
    assert reverseint(-15) == -51
    assert reverseint(-90) == -9
    assert reverseint(-2359) == -9532
