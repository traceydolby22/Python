results = [
    {"name": "test_login_valid_user",         "status": "pass"},
    {"name": "test_login_wrong_password",      "status": "fail"},
    {"name": "test_campaign_loads",            "status": "pass"},
    {"name": "test_campaign_empty_title",      "status": "fail"},
    {"name": "test_api_returns_200",           "status": "pass"},
    {"name": "test_api_missing_field",         "status": "fail"},
    {"name": "test_logout_clears_session",     "status": "pass"},
]

# 1. Count passes and failures

failed_tests = []
passed_tests = [] 
for result in results: 
    if result["status"] == "pass":
        passed_tests.append(result["name"])
    else: 
        failed_tests.append(result["name"])
# 2. Print names of failed tests
for name in failed_tests: 
    print(f" - {name}")
# 3. Print summary: "X of Y tests failed"
#print(f"Summary: {len(failed_tests)} in {len(results)} tests" )
# 4. Bonus: print pass rate percentage pass_rate = (len(passed_tests) / len(results)) * 100
pass_rate = len(passed_tests) / len(results) * 100
#print(f"Pass Rate: {pass_rate:.1f}%")

sample_records = [
    {"id": 1,    "title": "Summer Campaign", "body": "NA users", "userId": 3},
    {"id": 2,    "title": "",                "body": "EMEA",     "userId": 1},
    {"id": "x",  "title": "Holiday Promo",   "body": "All",      "userId": 2},
    {"id": 4,    "title": "Back to School",  "body": "EDU",      "userId": 0},
    {"title": "Missing ID campaign",          "body": "test",     "userId": 1},
]
REQUIRED_FIELDS = ["id", "title", "body", "userId"]
ids = []
userIds = [] 

def has_required_fields(record, fields):
    # return True if all fields present, False if any missing
    missing_fields = []
    for field in fields: 
        if field not in record or record[field] is None or record[field] == "":
            missing_fields.append(field)
        if missing_fields: 
            print(f" missing fields: {missing_fields}")
            return False
        return True
       
def is_valid_campaign(record):
    # check id is int, title is non-empty string, userId > 0
    if not has_required_fields(record, REQUIRED_FIELDS):
        return False
    if not isinstance(record["id"], int):
        print(f"  'id' must be an int, got: {type(record["id"]).__name__}")
        return False
    if not isinstance(record["title"], str) or len(record["title"].strip()) == 0:
        print(f"  'title' is empty or not a string")
        return False
    if not isinstance(record["userId"], int) or record["userId"] <= 0:
        print(f"  'userId' must be an int, got: {record["id"]}")
        return False
    return True

# Call your functions on each record and print results
for i, record in enumerate(sample_records):
    print(f"\nRecord {i + 1}:")
    result = is_valid_campaign(record)
    print(f" Result: {'√ Valid' if result else 'x Invalid'}")
#Bonus: print exactly which field failed and why
