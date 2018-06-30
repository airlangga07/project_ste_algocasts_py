from reversestring import reversestring

def test_reverse_reverses_a_string_no_whitespace():
    assert reversestring('abcd') == 'dcba'

def test_reverse_reverses_a_string_with_whitespace():
    assert reversestring('  abcd') == 'dcba  '

