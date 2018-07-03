from palindrome import palindrome

def test_aba_is_palindrome():
    assert palindrome('aba') == True

def test__aba_is_not_palindrome():
    assert palindrome(' aba') == False

def test_aba__is_not_palindrome():
    assert palindrome('aba ') == False

def test_greetings_is_not_palindrome():
    assert palindrome('greetings') == False

def test_1000000001_is_palindrome():
    assert palindrome('1000000001') == True

def test_Fish_hsif_is_not_palindrome():
    assert palindrome('Fish hsif') == False

def test_pennep_is_palindrome():
    assert palindrome('pennep') == True

