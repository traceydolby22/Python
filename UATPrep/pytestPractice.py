import pytest
from UATPrep.moreCodingPractice import is_eligible, validate_product, get_delivery_report, should_block_release

valid_user = {"id": "u1", "age": 27, "region": "US", "subscribed": True, "account_status": "active"}
#is_eligible(valid_user)
def test_eligible_user_passes():
    assert is_eligible(valid_user) == True

def test_underage_user_fails():
    user = {**valid_user, "age": 16}   # - just means "copy everything from valid_user and change age to 16
    assert is_eligible(user) == False

# this is the same as above {**valid_user} 
#def test_underage_user_fails():
    #user = {"id": "u1", "age": 16, "region": "US", 
         #   "subscribed": True, "account_status": "active"}
   # assert is_eligible(user) == False

def test_wrong_region_fails():
    user = {**valid_user, "region": "DE"}  
    assert is_eligible(user) == False# make a user with region "DE" and assert is_eligible returns False

def test_suspended_account_fails():
    user = {**valid_user, "account_status": "suspended"} 
    assert is_eligible(user) == False 



def test_valid_product_has_no_errors():
    product = {"id": "p1", "name": "iCloud", "price" : 2.99, "category": "storage", "active": True}
    result = validate_product(product)
    assert result["valid"] == True
    assert result["errors"] == [] # errors list must be empty, not missing

def test_empty_name_adds_error():
    product = {"id": "p2", "name": "", "price" : 9.99, "category": "musuc", "active": True}
    result = validate_product(product)
    assert result["valid"] == False
    assert len(result["errors"]) > 0

def test_negative_price_adds_error():
    # price: -1, assert valid is False and errors is not empty
    product = {"id": "p3", "name": "Apple One", "price": -1, "category": "bundle", "active": True}
    result = validate_product(product)
    assert result["valid"] == False
    assert result["errors"] != []

def test_multiple_failures_caught():
    # name: "" AND price: -1, assert len(errors) == 2
    product = {"id": "p4", "name": "", "price": -1, "category": "music", "active": True}
    result = validate_product(product)
    assert result["valid"] == False
    assert len(result["errors"]) == 2 

@pytest.fixture
def sample_notifications():
    return [ 
        {"id": "n1", "status": "delivered", "platform": "iOS"},
        {"id": "n2", "status": "failed",    "platform": "Android"},
        {"id": "n3", "status": "delivered", "platform": "iOS"},
        {"id": "n4", "status": "pending",   "platform": "iOS"},
        {"id": "n5", "status": "delivered", "platform": "Android"},
    ]
def test_total_count(sample_notifications):
    report = get_delivery_report(sample_notifications)
    assert report["total"] == 5

def test_delivered_count(sample_notifications):
    report = get_delivery_report(sample_notifications)
    assert report["delivered"] == 3

def test_failures_list_contains_correct_id(sample_notifications):
    report = get_delivery_report(sample_notifications)
    assert "n2" in report["failures"]

def test_delivery_rate(sample_notifications):
    report = get_delivery_report(sample_notifications)
    assert report["delivery_rate"] == 60.0

def test_blocks_when_tests_failed():
    summary = {"failed": 2, "pass_rate": 57.1, "failed_tests": ["test_a"]}
    assert should_block_release(summary) == True

def test_blocks_when_pass_rate_low():
    summary = {"failed": 0, "pass_rate": 75.0, "failed_tests": []}
    assert should_block_release(summary) == True

def test_passes_when_all_good():
    summary = {"failed": 0, "pass_rate": 100.0, "failed_tests": []}
    assert should_block_release(summary) == False

# Bonus: rewrite the 3 tests above as one parametrized test
@pytest.mark.parametrize("failed, pass_rate, expected", [
    (2,  57.1,  True),    # failures exist
    (0,  75.0,  True),    # pass rate too low
    (0, 100.0, False),    # all good
])
def test_block_release_cases(failed, pass_rate, expected):
    # build the summary dict and assert should_block_release returns expected
    summary = {"failed": failed, "pass_rate": pass_rate, "failed_tests" : []}
    assert should_block_release(summary) == expected
   