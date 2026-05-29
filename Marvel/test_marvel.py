import pytest
from marvelCharacter import get_low_stat_heroes, get_super_strength_heroes, marvelCharacters, get_heroes_with_shared_powers, get_heroes_by_power_tier

def test_low_stat_heroes_returns_correct_names():
    result = get_low_stat_heroes(marvelCharacters) 
    assert "Nick Fury" in result
    assert "Carol Danvers" not in result

def test_low_stats_descend():
    result = get_low_stat_heroes(marvelCharacters)
    assert result == ['Nick Fury', 'Steven Strange', 'Groot', 'Loki', 'Rocket']

def test_super_strength_returns_correct_names():
    result =  get_super_strength_heroes(marvelCharacters)
    assert "Steve Rogers" in result
    assert "Carol Danvers" in result
    assert "Groot" in result 
     

def test_super_strength_exclues_others():
    result =  get_super_strength_heroes(marvelCharacters)
    assert "Loki" not in result 
    assert "Nick Fury" not in result

def test_heroes_by_power_tier():
    result = get_heroes_by_power_tier(marvelCharacters)
    assert "Steve Rogers" in result["elite"]
    assert "Tony Stark" in result["mid"]
    assert "Loki" in result["low"]

def test_heroes_with_shared_powers():
    result = get_heroes_with_shared_powers(marvelCharacters)
    assert "super human strength" in result
    assert "combat fighting" not in result
    assert "Steve Rogers" and "Carol Danvers" in result["super human strength"]

