import pytest
from unittest.mock import patch
from two_a import *

def test_instance_possible_all_possible():
    test_instance = {'red': 1, 'blue': 2, 'green': 3}
    assert instance_possible(test_instance) == True 

def test_isntance_possible_one_color_high():
    test_instance = {'red': 1, 'blue': LEGEND['blue'] + 1, 'green': 3}
    assert instance_possible(test_instance) is False

def test_instance_possible_one_color_equal_to_limit():
    test_instance = {'red': 1, 'blue': 2, 'green': LEGEND['green']}
    assert instance_possible(test_instance) is True

@patch('two_a.instance_possible', return_value=True)
def test_game_possible_all_games_possible(mock_instance_possible):
    line = 'Game 13: 11 red, 12 blue, 7 green; 20 red, 12 green, 9 blue; 11 red, 5 green, 11 blue'
    assert game_possible(line) > 0


def test_game_possible_one_game_impossible():
    line = 'Game 13: 11 red, 12 blue, 7 green; 20 red, 12 green, 9 blue; 11 red, 5 green, 11 blue;'
    assert game_possible(line) == 0