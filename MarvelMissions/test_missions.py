import pytest

from missions import get_failed_missions, get_experienced_heroes, get_mission_counts , get_overlapping_missions, missions

def test_overlaping_missions():
    result = get_overlapping_missions(missions)
    assert "Operation Ironclad" in result["Operation Nightfall"]
    assert "Operation Starfall" not in result["Operation Nightfall"]

def test_hero_in_mission():
    result = get_experienced_heroes(missions)
    assert "Steve Rogers" in result
    assert "Loki" not in result 

def test_failed_missions_returns_four():
    result = get_failed_missions(missions)
    assert len(result) == 4
    assert result[0]["difficulty"] == 115
