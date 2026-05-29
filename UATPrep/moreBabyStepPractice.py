# Think of a function like a vending machine. You put one coin in, you get one answer out. 
# You don't pour the whole bag of coins in at once. The loop outside is what feeds coins in one at a time.

numbers = [5, -1, 0, 42, -7, 3]
words = ["hi", "hello", "ok", "campaign", "a", "test"]

def is_positive(number):
    return number > 0

def is_long_enough(word):
    return len(word) > 3

for num in numbers: 
    print(f"{num}: {is_positive(num)}") 
for word in words: 
    print(f"{word}: {is_long_enough(word)}") 

# Think of it like a checklist before a flight. You don't call the plane airworthy after checking one item. 
# You go through the whole list, then make the call at the end.

numbers_a = [5, 3, 8, 1, 2]
numbers_b = [5, 3, -1, 1, 2]
words_a = ["hello", "world", "ok"]
words_b = ["hello", "", "ok"]

def all_positive(numbers):
     for number in numbers: 
        if number <= 0: 
            return False
     return True


def has_no_empty_strings(words):
    for word in words: 
        if word == "":
            return False 
    return True

#print(all_positive(numbers_b))
#print(has_no_empty_strings(words_a))

#This combines both drills: write a function that takes one record, validates it, 
# then call it on a list of records one at a time. This is exactly what Exercise 2 asked 
# for — now you have the pieces to do it cleanly.

users = [
    {"name": "Tracey",  "age": 32, "email": "tracey@gmail.com"},
    {"name": "",        "age": 25, "email": "no-name@gmail.com"},
    {"name": "Jordan",  "age": -1, "email": "jordan@gmail.com"},
    {"name": "Alex",    "age": 28, "email": "not-an-email"},
    {"name": "Morgan",  "age": 30, "email": "morgan@apple.com"},
]

def is_valid_user(user):
    if user["name"] == "" :   
        return False
    if user["age"] <= 0 :   
        return False
    if "@" not in user["email"] : 
        return False
    return True
invalid_user = []
for user in users: 
    valid = is_valid_user(user)
    print(f"{user['name']or '(no name)'}: {valid}")
    if not valid: 
        invalid_user.append(user)
#print(f"\n{len(invalid_user)} invalid user(s):")
for u in invalid_user:
    print(f"  - {u}")


bugs = [
    {"title": "Payment timeout",      "severity": "high",   "status": "open",     "affected_users": 5000},
    {"title": "Login button missing", "severity": "high",   "status": "resolved", "affected_users": 2000},
    {"title": "Slow load time",       "severity": "medium", "status": "open",     "affected_users": 500},
    {"title": "Campaign not sending", "severity": "high",   "status": "open",     "affected_users": 15000},
    {"title": "Typo in footer",       "severity": "low",    "status": "open",     "affected_users": 10},
]

def is_critical(bug) :
    if bug["severity"] != "high":
        return False
    if bug["status"] == "resolved":
        return False
    if bug["affected_users"] <= 1000:
        return False
    return True

critical_count = 0 
for bug in bugs: 
    result = is_critical(bug)
    print(f"{bug['title']}, {'🔴 CRITICAL' if result else '✓ ok'}")
    if result: 
        critical_count += 1
#print(f"\n{critical_count} critical bug(s) need immediate escalation")


results = [
    {"name": "test_login",          "status": "pass", "duration_ms": 120},
    {"name": "test_payment_flow",   "status": "fail", "duration_ms": 340},
    {"name": "test_campaign_loads", "status": "pass", "duration_ms": 95},
    {"name": "test_empty_cart",     "status": "fail", "duration_ms": 210},
    {"name": "test_logout",         "status": "pass", "duration_ms": 80},
    {"name": "test_api_timeout",    "status": "fail", "duration_ms": 5000},
    {"name": "test_profile_update", "status": "pass", "duration_ms": 150},
]

new_list = []
def get_summary(results):
    # loop INSIDE — this function owns the whole list
    passed = 0
    failed = 0
    
    for result in results:
        if result["status"] == "pass":
            passed += 1
        else: 
            failed += 1
    
    # return a dict with keys: total, passed, failed, pass_rate
    pass_rate = round(passed / len(results) * 100, 1)
    return {
        "total" : len(results),
        "passed" : passed, 
        "failed" : failed,
        "pass_rate" : pass_rate
    }


def get_failed_tests(results):
    # return a list of just the names of failed tests
    failed_list = [] 
    for result in results:
        if result["status"] == "fail":
            failed_list.append(result["name"])
    return failed_list
    

summary = get_summary(results)
# print each value from summary clearly
#print(summary["total"])
#print(summary["passed"])
#print(summary["failed"])
#print(summary["pass_rate"])
failed = get_failed_tests(results)
# print each failed test name
for name in failed : 
    print(f" - {name}")

responses = [
    {"status_code": 200, "data": [{"id": 1, "title": "Campaign A"}]},
    {"status_code": 404, "data": None},
    {"status_code": 200, "data": []},
    {"status_code": 200, "data": [{"id": 2, "title": "Campaign B"}]},
    {"status_code": 500},
]

def is_valid_response(response):
        if "data" not in response: 
            return False 
        if response["status_code"] != 200 :
            return False
        if response["data"] == None:
            return False
        if len(response["data"]) == 0:
            return False
        return True

for i, response in enumerate(responses):
    print(f"Response {i + 1}: {is_valid_response(response)}")
 
