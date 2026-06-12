import pytest

from students import students, get_student_names_by_subject, get_name_of_student_with_highest_score, get_average_score_per_grade

def test_student_names_by_subject():
    result = get_student_names_by_subject(students)
    assert "Maya Chen" in result["Math"]
    assert "Yuki Tanaka" in result["Math"]
    assert "James Park" in result["Science"]
    assert "Priya Nair" in result["Science"]
    assert "Derek Mills" in result["English"]
    assert "Tobias Grant" in result["English"]

def test_student_with_highest_score():
    result = get_name_of_student_with_highest_score(students)
    assert result == "Derek Mills"

def test_average_score_per_grade():
    result = get_average_score_per_grade(students)
    assert 79.0 == result[11]
    assert 80.0 == result[10]
    assert 89.67 == result[12]