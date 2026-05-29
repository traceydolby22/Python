#You're validating which users should receive a promotional campaign. 
# Write is_eligible(user) and get_eligible_users(users) that returns a summary dict.

ELIGIBLE_REGIONS = ["US", "CA", "GB"]

users = [
    {"id": "u1", "age": 22, "region": "US", "subscribed": True,  "account_status": "active"},
    {"id": "u2", "age": 16, "region": "US", "subscribed": True,  "account_status": "active"},
    {"id": "u3", "age": 34, "region": "DE", "subscribed": True,  "account_status": "active"},
    {"id": "u4", "age": 29, "region": "CA", "subscribed": False, "account_status": "active"},
    {"id": "u5", "age": 41, "region": "GB", "subscribed": True,  "account_status": "suspended"},
    {"id": "u6", "age": 27, "region": "US", "subscribed": True,  "account_status": "active"},
]
# Rules: age >= 18, region in ELIGIBLE_REGIONS,
# subscribed is True, account_status is "active"

def is_eligible(user):
    if user["age"] < 18:
        return False
    if user["region"] not in ELIGIBLE_REGIONS:
        return False
    if user["subscribed"] != True: 
        return False
    if user["account_status"] != "active":
        return False
    return True

def get_eligible(users):
    eligible_ids = [user["id"] for user in users if is_eligible(user)]
    ineligible_ids = [user["id"] for user in users if not is_eligible(user)]
    return {
        "eligible" : eligible_ids,
        "ineligible" : ineligible_ids,
        "total" : len(users)
    }
    #returns a summary dict. # return: { "eligible": [ids], "ineligible": [ids], "total": n }

# print(f"{get_eligible(users)}")

#You're testing an API that returns product data. 
# Write validate_product(product) that returns a dict with valid (bool) 
# and errors (list of strings describing each failure).
products = [
    {"id": "p1", "name": "iCloud+",     "price": 2.99,  "category": "storage",  "active": True},
    {"id": "p2", "name": "",            "price": 9.99,  "category": "music",    "active": True},
    {"id": "p3", "name": "Apple One",   "price": -1,    "category": "bundle",   "active": True},
    {"id": "p4", "name": "Apple TV+",   "price": 9.99,  "category": None,       "active": True},
    {"id": "p5", "name": "Apple News+", "price": 12.99, "category": "news",     "active": False},
    {"id": "p6", "name": "Arcade",      "price": 6.99,  "category": "gaming",   "active": True},
]

# Rules:
# - name must be a non-empty string
# - price must be a number > 0
# - category must not be None
# - active must be True (inactive = not shippable)
# validate_product should return {"valid": bool, "errors": [...]}
# errors list should be EMPTY (not missing) when valid
def validate_product(product):
    errors = [] 
    if len(product["name"]) == 0:
        errors.append("name is empty")
    if not isinstance(product["price"], (int,float)) or product["price"] <= 0: 
        errors.append("price must be > 0")
    if product["category"] is None:
        errors.append("category must not be None")
    if not product["active"]: 
        errors.append("active must be True")
    return {
        "valid" : len(errors) == 0,
        "errors" : errors
    }
    #returns a dict with valid (bool) and errors (list of strings describing each failure).

def get_invalid_product(products):
    for product in products: 
        result = validate_product(product)
        if not result["valid"]:
            print(f"{product["name"]}, errors: {result["errors"]}")
    
#print(f"{get_invalid_product(products)}")
#print(f"{validate_product(products[4])}")

# You're validating a batch push notification send. Write get_delivery_report(notifications) that groups results and calculates a delivery rate
notifications = [
    {"id": "n1",  "user_id": "u1", "status": "delivered", "platform": "iOS"},
    {"id": "n2",  "user_id": "u2", "status": "failed",    "platform": "Android"},
    {"id": "n3",  "user_id": "u3", "status": "delivered", "platform": "iOS"},
    {"id": "n4",  "user_id": "u4", "status": "pending",   "platform": "iOS"},
    {"id": "n5",  "user_id": "u5", "status": "delivered", "platform": "Android"},
    {"id": "n6",  "user_id": "u6", "status": "failed",    "platform": "iOS"},
    {"id": "n7",  "user_id": "u7", "status": "delivered", "platform": "Android"},
    {"id": "n8",  "user_id": "u8", "status": "delivered", "platform": "iOS"},
]
def get_delivery_report(notifications):
    delivered = 0 
    failed = 0 
    pending = 0 
    failures = [] 
    for notifs in notifications: 
        if notifs["status"] == "delivered":
            delivered += 1 
        if notifs["status"] == "failed":
            failed += 1 
            failures.append(notifs["id"])
        if notifs["status"] == "pending":
            pending += 1 
    return {
        "total" : len(notifications),
        "delivered" : delivered,
        "failed" : failed,
        "pending" : pending,
        "failures" : failures,
        "delivery_rate" : round(delivered / len(notifications) * 100, 1)
    }
# get_delivery_report should return:
# {
#   "total": 8,
#   "delivered": 5,
#   "failed": 2,
#   "pending": 1,
#   "delivery_rate": 62.5,      ← delivered / total * 100, rounded to 1 decimal
#   "failures": ["n2", "n6"]    ← ids of failed notifications
# }
#print(f"{get_delivery_report(notifications)}")

# This one mirrors what pytest does internally. Write get_test_summary(results) and a should_block_release(summary) 
# function that uses the summary to make a go/no-go call.
test_results = [
    {"name": "test_login_valid",        "status": "passed",  "duration_ms": 120},
    {"name": "test_login_empty_pass",   "status": "passed",  "duration_ms": 95},
    {"name": "test_checkout_flow",      "status": "failed",  "duration_ms": 340},
    {"name": "test_payment_processing", "status": "passed",  "duration_ms": 512},
    {"name": "test_promo_apply",        "status": "failed",  "duration_ms": 88},
    {"name": "test_profile_update",     "status": "skipped", "duration_ms": 0},
    {"name": "test_logout",             "status": "passed",  "duration_ms": 44},
]

def get_test_summary(results):
    passed = 0
    failed = 0 
    skipped = 0 
    failed_tests = [] 
    total_duration = 0
    non_skipped_count = 0
# get_test_summary returns:
    for result in results: 
        if result["status"] == "passed":
            passed += 1
        if result["status"] == "failed":
            failed += 1
            failed_tests.append(result["name"])
        if result["status"] == "skipped":
            skipped += 1
# complex way to write Python for figuring out the average_duration
#non_skipped = [r for r in results if r["status "] != "skipped"]
#total_duration = sum(r["duration_ms"] for r in non_skipped)
#avg = round(total_duration / len(non_skipped))
    for result in results:
        if result["status"] != "skipped":
            total_duration += result["duration_ms"]
            non_skipped_count += 1

    avg = round(total_duration / non_skipped_count, 1)

    return {
        "total" : len(results),
        "failed" : failed,
        "passed" : passed,
        "skipped" : skipped,
        "pass_rate" : round(passed / len(results) * 100, 1),
        "average_duration" : avg,
        "failed_tests" : failed_tests
    }
def should_block_release(summary):

    if summary["failed"] > 0:
        return True
    if summary["pass_rate"] < 80.0: 
        return True 
    return False


summary = get_test_summary(test_results)  
print(summary)

print(f"Block Release: {should_block_release(summary)}")