def add_two_numbers(a, b):
    return a + b

def test_add_two_numbers():
    expected = 10
    actual = add_two_numbers(5, 5)
    assert expected == actual

def test_pos_neg_numbers():
    expected = 3
    actual = add_two_numbers(6, -3)
    assert expected == actual

def test_float_float_numbers():
    expected = 10.0                     # we also can use 10 but i aint sire of the number is an int or a float
    actual = add_two_numbers(6.4, 3.6)
    assert expected == actual
#... This is what i wrote.
def test_string_whole_numbers():
    expected = TypeError                  # LOOK INTO THIS, BEN SAYS ITS SHOULDNT BE WORKING
    actual = add_two_numbers("Hello", 3)  # add code into the original FUNC abov on line(1/2)
    assert expected == actual             # 
#... This is what Junaid wrote.
def test_string_whole_numbers():
    try:
        expected = TypeError                  # LOOK INTO THIS, BEN SAYS ITS SHOULDNT BE WORKING
        actual = add_two_numbers("Hello", 3)
        assert expected == actual
    except:
        print('Wrong input')
#... Check what Ben writes
def test_string_string_numbers():
    expected = "Hello There"
    actual = add_two_numbers("Hello", " There")
    assert expected == actual



1.
def add_two_numbers(a, b):
    return a + b
def test_adds_two_whole_numbers():
    expected = 2
    actual = add_two_numbers(1, 1)
    assert expected == actual
test_adds_two_whole_numbers()

2.
def add_two_numbers(a, b):
    return a + b
def test_adds_pos_neg_numbers():
    expected = 0
    actual = add_two_numbers(-100, 100)
    assert expected == actual
test_adds_pos_neg_numbers()

3.
def add_two_numbers(a, b):
    return a + b
def test_adds_two_fp_numbers():
    expected = 0.9
    actual = add_two_numbers(0.5, 0.4)
    assert expected == actual
test_adds_two_fp_numbers()

4.
def add_two_numbers(a, b):
    try:
        return a + b
    except:
        return "Invalid Input"

def test_adds_string_to_number():
    expected = "Invalid Input"
    actual = add_two_numbers("test", 1)
    assert expected == actual
test_adds_string_to_number()

5.
def add_two_numbers(a, b):
    if not instanceof(a, int) or not instanceof(b, int):   # I
        return "Invalid input"
        return a + b

def test_adds_two_strings():
    expected = "Invalid Input"
    actual = add_two_numbers("test", "case")
    assert expected == actual
test_adds_two_strings()