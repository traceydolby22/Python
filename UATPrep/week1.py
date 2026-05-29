flags = [
    {"name": "new_checkout",   "enabled": True,  "rollout": {"percentage": 100, "regions": ["US", "CA"]}},
    {"name": "dark_mode",      "enabled": True,  "rollout": {"percentage": 50,  "regions": ["US"]}},
    {"name": "beta_payments",  "enabled": False, "rollout": {"percentage": 0,   "regions": []}},
    {"name": "new_onboarding", "enabled": True,  "rollout": {"percentage": 110, "regions": ["US"]}},
    {"name": "promo_banner",   "enabled": True,  "rollout": {"percentage": 25,  "regions": []}},
]

def is_flag_valid(flag):
    # - enabled must be True
    if flag["enabled"] != True:
        return False
    # - rollout percentage must be between 0 and 100 (inclusive)
    if flag["rollout"]["percentage"] < 0 and flag["rollout"]["percentage"] > 101:
        return False
    # - regions list must not be empty if enabled is True
    if len(flag["rollout"]["regions"]) == 0:
        return False
    return True 

def get_flag_report(flags):
    valid = []
    invalid = [] 
    for flag in flags: 
        if is_flag_valid(flag): 
            valid.append(flag["name"])
        else: 
            invalid.append(flag["name"])
    return {
        "valid" : valid,
        "invalid" : invalid,
        "total" : len(flags)
    }
    # get_flag_report returns:
# { "valid": [names], "invalid": [names], "total": n }
#print(f"{get_flag_report(flags)}")

last_week = [
    {"name": "test_login",        "status": "passed"},
    {"name": "test_checkout",     "status": "passed"},
    {"name": "test_payment",      "status": "passed"},
    {"name": "test_profile",      "status": "failed"},
    {"name": "test_search",       "status": "passed"},
]

this_week = [
    {"name": "test_login",        "status": "passed"},
    {"name": "test_checkout",     "status": "failed"},
    {"name": "test_payment",      "status": "failed"},
    {"name": "test_profile",      "status": "failed"},
    {"name": "test_search",       "status": "passed"},
]

def find_regression(last_week, this_week):
    regressions = []  
    stable_failures = [] 
    last_check = {}

    for test in last_week:
        last_check[test["name"]] = test["status"]

    for test in this_week: 
        last_week_results = last_check[test["name"]]
        if last_week_results == "passed" and test["status"] == "failed":
            regressions.append(test["name"])
        if last_week_results == "failed" and test["status"] == "failed":
            stable_failures.append(test["name"])

    return {
        "regressions": regressions,
        "regression_count" : len(regressions),
        "stable_failures" : stable_failures
    }
    # find_regressions returns:
# {
#   "regressions": [test names],
#   "regression_count": n,
#   "stable_failures": [names that failed both weeks]
# }
#print(f"{find_regression(last_week, this_week)}")

messages = [
    {"id": "m1", "title": "Big Sale!",  "body": "Get 50% off today only.", "deep_link": "app://sale"},
    {"id": "m2", "title": "",           "body": "Check this out.",          "deep_link": "app://home"},
    {"id": "m3", "title": "Hey there!", "body": "",                         "deep_link": "app://home"},
    {"id": "m4", "title": "New drop!",  "body": "Something new is here.",   "deep_link": "http://sale"},
    {"id": "m5", "title": "X" * 65,    "body": "Short body.",               "deep_link": "app://home"},
]
def validate_message(message):

    errors = [] 
# - title must not be empty
    if len(message["title"]) == 0: 
        errors.append("title is empty")
# - title must be 64 characters or fewer
    if len(message["title"]) > 64: 
        errors.append("title has more than 64 chars")
# - body must not be empty
    if len(message["body"] ) == 0: 
        errors.append("body is empty ")
# - deep_link must start with "app://"
    if not message["deep_link"].startswith("app://"):
       errors.append("deep_link doesn't start with app://")

    return {
        "valid" : len(errors) == 0,
        "errors" : errors
    }
# validate_message returns {"valid": bool, "errors": [...]}
# Hint: "app://home".startswith("app://") → True
# Hint: len("hello") → 5
#print(f"{validate_message(messages[0])}")
#for message in messages: 
   # print(validate_message(message))

release_data = {
    "environments": [
        {"name": "prod-us", "status": "active", "health": "passing"},
        {"name": "prod-eu", "status": "active", "health": "failing"},
    ],
    "test_results": [
        {"name": "test_login",    "status": "passed"},
        {"name": "test_payment",  "status": "failed"},
        {"name": "test_checkout", "status": "passed"},
    ],
    "feature_flags": [
        {"name": "new_checkout", "enabled": True,  "rollout": 100},
        {"name": "dark_mode",    "enabled": True,  "rollout": 50},
    ]
}

def get_release_readiness(data):
    nogo = []
    tests_passing = []
    flags_valid = True
    for env in data["environments"]:
        if env["health"] == "failing":
            nogo.append(env["name"])
        else: 
            tests_passing.append(env["name"])
    
    for test in data["test_results"]:
        if test["status"] == "failed":
            nogo.append(test["name"])
        else: 
            tests_passing.append(test["name"])
    
    for flag in data["feature_flags"]:
        if flag["rollout"] <= 0:
            return False
        else: 
            flags_valid
        
    return {
        "go" : len(nogo) == 0,
        "reasons" : nogo,
        "environment_healthy" : all(env["health"] == "passing" for env in data["environments"]),
        "tests_passing" : len(tests_passing) != 0,
        "flags_valid" :  flags_valid
    }
    #"go": bool,            ← False if ANY of the below are true
#   "reasons": [...],      ← list of reasons why it's a no-go (empty if go)
#   "environments_healthy": bool,   ← all active envs passing
#   "tests_passing": bool,          ← no failed tests
#   "flags_valid": bool             ← all enabled flags have rollout > 0
print(get_release_readiness(release_data))