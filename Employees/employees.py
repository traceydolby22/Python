import json 

with open("employees.json", "r") as f:
    employees = json.load(f)

def get_active_engineers(employees):
    active_employees = []
    for employee in employees: 
        if employee["status"] == "active" and employee["department"] == "Engineering":
            active_employees.append(employee["employee"])
    # Return a list of names of active employees
    # in the Engineering department
    return active_employees

def get_average_salary_by_department(employees):
    department_count = {} 
    department_salary = {}
    for employee in employees: 
        if employee["department"] not in department_salary:
            department_salary[employee["department"]] = 0
        department_salary[employee["department"]] += employee["salary"]
     

    for employee in employees: 
        department = employee["department"]
        if department not in department_count:
            department_count[department] = 0 
        department_count[department] += 1
    result = {}
    for department in department_salary:
         result[department] = department_salary[department] / department_count[department] 
    return result
    # Return a dict with each department's average salary
    # rounded to 2 decimal places
    # {"Engineering": 98750.00, "Marketing": ..., "HR": ...}

def employees_with_skills(employees, skill):
    employee_skill = [] 
    for employee in employees: 
        if skill in employee["skills"]:
            employee_skill.append(employee["employee"])
    return employee_skill 
     # Given a skill string, return a list of 
    # names of ALL employees who have that skill
    # regardless of status
    
def get_seniority_report(employees):
    junior_employees = []
    mid_employees = [] 
    senior_employees = [] 
    for employee in employees: 
        if employee["years"] < 3: 
            junior_employees.append(employee["employee"])
        elif employee["years"] >= 3 and  employee["years"] <= 6:
            mid_employees.append(employee["employee"])
        elif employee["years"] > 6:
            senior_employees.append(employee["employee"])
# Return a dict with three keys:
    # "junior": employees with less than 3 years
    # "mid": employees with 3-6 years inclusive
    # "senior": employees with more than 6 years
    # Each key maps to a list of employee names
    return {
        "junior" : junior_employees,
        "mid" : mid_employees,
        "senior" : senior_employees
    }
    
#print(get_active_engineers(employees)) 
#print(get_average_salary_by_department(employees))     
#print(employees_with_skills(employees, "analytics"))
print(get_seniority_report(employees))   

def get_employees_by_department(employees):
    department_list = {}
    for employee in employees:
        dept = employee["department"]
        if dept not in department_list:
            department_list[dept] = []
        department_list[dept].append(employee["employee"])
    return department_list

def get_highest_paid_employee(employees):
    highest_salary = 0
    top_employee = ""
    for employee in employees:
        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            top_employee = employee["employee"]
    return top_employee

def get_average_tenure(employees):
    total_years = {}
    count_years = {}
    for employee in employees:
        dept = employee["department"]
        if dept not in total_years:
            total_years[dept] = 0
            count_years[dept] = 0 
        total_years[dept] += employee["years"]
        count_years[dept] += 1
    
    average = {}
    for total in total_years:
        average[total] = round(total_years[total] / count_years[total], 2)
    return average

print(get_highest_paid_employee(employees))