import pytest
from pets import pets, group_pets_by_type, get_first_alphabetical_pet, get_average_age_by_type

def test_pets_by_type():
    result = group_pets_by_type(pets)
    assert "Luna" in result["dog"]
    assert "Rex" in result["dog"]
    assert "Buddy" in result["dog"]
    assert "Luna" not in result["cat"]
    assert "Mochi" in result["cat"]
    assert "Bella" in result["cat"]
    assert "Whiskers" in result["cat"]

def test_first_alphabetical_pet():
    result = get_first_alphabetical_pet(pets)
    assert result == "Luna"

def test_average_age_of_pet_by_type():
    result = get_average_age_by_type(pets)
    assert 4.67 == result["dog"]
    assert 5.0 == result["cat"]

