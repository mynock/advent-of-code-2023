from one_a import *
import pytest

def test_number_first():
    assert numbers_from_string("1a2d") == 12

def test_letter_first():
    assert numbers_from_string("b1a2d") == 12

def test_more_than_2_numbers():
    assert numbers_from_string("1a2d3c4") == 14

def test_only_one_number():
    assert numbers_from_string("ex1a") == 11

def test_only_letters():
    assert numbers_from_string("abd") == 0

def test_with_worded_numbers():
    assert(numbers_from_string("one3threerabble4") == 14)

def test_input_string():
    assert(numbers_from_string("ldklqc91fiveeighteight9") == 99)
