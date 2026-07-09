import json

with open("nestedData.json", "r") as nd:
    results = json.load(nd)


#Given a list of test run IDs where some runs were executed multiple times, return a list of unique IDs in the order they FIRST appeared — no duplicates, original order maintained.
list_of_ids = ["T001", "T002", "T001", "T003", "T002", "T004"] #→ ["T001", "T002", "T003", "T004"]
#No using set() directly — that doesn't preserve order. Think about what data structure would let you track what you've already seen.
def unique_Id(ids):
    id_in_order = []
    for id in ids:
        if id not in id_in_order:
            id_in_order.append(id)
    return id_in_order
#print(unique_Id(list_of_ids))

def get_failed_tests_by_suite(results):
    # Return a dict of suite names mapping to 
    # a list of FAILED test names only
    # {"auth": ["login_invalid"], "payments": ["checkout_decline", "refund"]}
    # Only include suites that have at least one failure
    suite_names = {}
    
    for result in results: 
        suite = result["suite"]
        tests = result["tests"]    
        for test in tests: 
            test_name = test["name"]
            if test["status"] == "fail":
                if suite not in suite_names: 
                    suite_names[suite] = []
                suite_names[suite].append(test_name)
    return suite_names
print(get_failed_tests_by_suite(results))

#Given a list of test names in snake_case, return a new list where each name is converted to Title Case with spaces, and any test name containing the word "skip" is excluded entirely.
manipulate_string = ["test_login_flow", "test_skip_payment", "test_checkout_success", "skip_broken_feature"]
#→ ["Test Login Flow", "Test Checkout Success"]
def string_manipulator(string):
    new_list = [text.replace("_", " ").title() for text in string if "skip" not in text]

    return new_list
    
print(string_manipulator(manipulate_string))      