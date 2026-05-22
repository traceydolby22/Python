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
print(f"Summary: {len(failed_tests)} in {len(results)} tests" )
# 4. Bonus: print pass rate percentage pass_rate = (len(passed_tests) / len(results)) * 100
pass_rate = len(passed_tests) / len(results) * 100
print(f"Pass Rate: {pass_rate:.1f}%")