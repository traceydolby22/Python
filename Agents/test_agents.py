import pytest
from agents import agents, get_elite_agents, get_shared_skills, get_readiness_report, group_by_clearace, get_status_summary, get_mision_summary

def test_elite_agents_list():
    result = get_elite_agents(agents)
    assert "Fatima Al-Hassan" in result
    assert "Yuki Tanaka" in result
    assert "Maya Chen" in result
    assert "James Okafor" not in result 

def test_shared_skills_list():
    result = get_shared_skills(agents)
    assert "hacking" in result
    assert "explosives" in result
    assert "Sofia Reyes" in result["hacking"]
    assert "Priya Nair" in result["psychology"]

def test_group_by_clearance_list():
    result = group_by_clearace(agents)
    assert "Yuki Tanaka" in result[9]
    assert "Carlos Mendez"in result[5]
    assert "Fatima Al-Hassan" in result[10]

def test_mission_summary():
    result = get_mision_summary(agents)
    assert 379 == result["total_missions"]
    assert "Fatima Al-Hassan" == result["most_experienced"]
    assert "Erik Strand" != result["least_experienced"] 
    assert 37.9 == result["average_missions"]

def test_status_summary():
    result = get_status_summary(agents)
    assert 7 == result["active"]
    assert 2 == result["inactive"]
    assert 1 == result["suspended"]


    