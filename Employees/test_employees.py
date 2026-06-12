import pytest

from employees import employees, get_seniority_report, employees_with_skills, get_active_engineers, get_average_salary_by_department

def test_get_active_engineers():
    result = get_active_engineers(employees)
    assert "Jordan Lee" in result
    assert "Derek Okafor" in result 
    assert "Sofia Chen" not in result 

def test_employees_with_skills():
    python_check = employees_with_skills(employees, "python")
    recruiting_check = employees_with_skills(employees, "recruiting")
    sql_check = employees_with_skills(employees, "sql")
    javascript_check = employees_with_skills(employees, "javascript")
    seo_check = employees_with_skills(employees, "seo")
    copywrite_check = employees_with_skills(employees, "copywriting")
    analytics_check = employees_with_skills(employees, "analytics")
    assert "Jordan Lee" in python_check 
    assert "Derek Okafor" in python_check
    assert "Sofia Chen" in recruiting_check
    assert "Lena Kovac" in recruiting_check
    assert "Jordan Lee" in sql_check
    assert "Tobias Grant" in sql_check
    assert "Jordan Lee" in javascript_check
    assert "Derek Okafor" in javascript_check
    assert "Amara Singh" in seo_check
    assert "Yara Osei" in seo_check
    assert "Priya Patel" in copywrite_check
    assert "Yara Osei" in copywrite_check
    assert "Amara Singh" in analytics_check
    assert "Finn Murphy" in analytics_check


def test_avg_salary_by_dept():
    result = get_average_salary_by_department(employees)
    assert 98750.0 == result["Engineering"]
    assert 71000.0 == result["HR"]

def test_get_seniority_report():
    result = get_seniority_report(employees)
    assert "Priya Patel" in result["junior"]
    assert "Yara Osei" in result["junior"]
    assert "Sofia Chen" in result["mid"]
    assert "Finn Murphy" in result["mid"]
    assert "Marcus Webb" in result["senior"]
    assert "Tobias Grant" in result["senior"]