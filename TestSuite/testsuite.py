import json 

with open("testsuite.json", "r") as ts:
    test_runs = json.load(ts)

def get_failed_tests(test_runs):
    # Return a list of test names with status "failed"
    failedTests = []
    for tests in test_runs:
        if tests["status"] == "failed":
            failedTests.append(tests["test_name"])
    return failedTests 
    


def group_tests_by_suite(test_runs):
    # Group test names by suite
    # {"auth": [...], "payments": [...], "profile": [...]}
    testSuiteList = {}
    for tests in test_runs:
        testSuite = tests["suite"]
        if testSuite not in testSuiteList:
            testSuiteList[testSuite] = []
        testSuiteList[testSuite].append(tests["test_name"])
    return testSuiteList

def get_slowest_test(test_runs):
    # Return the name of the test with the highest duration_sec
    highestDuration = 0
    testWithHighDuration = ""
    for tests in test_runs:
        name = tests["test_name"]
        duration = tests["duration_sec"]
        if highestDuration < duration:
            highestDuration = duration
            testWithHighDuration = name
    return testWithHighDuration

def get_average_duration_by_suite(test_runs):
    # Return average duration_sec per suite, rounded to 2 decimal places
    durationPerSuite = {}
    count = {}
    suiteList = {}
    for tests in test_runs:
        duration = tests["duration_sec"]
        suite = tests["suite"]
        if suite not in suiteList:
            suiteList[suite] = 0
            count[suite] = 0 
        
        suiteList[suite] += duration
        count[suite] += 1
    for average in suiteList:
        durationPerSuite[average] = round(suiteList[average]/count[average], 2)
    return durationPerSuite
print(get_average_duration_by_suite(test_runs))  

def get_flaky_failed_tests(test_runs):
    # Return names of tests that are BOTH flaky AND currently failed
    # This simulates prioritizing which flaky tests need urgent attention
    flakyFailedTests = []
    for tests in test_runs:
        if tests["status"] == "failed":
            if tests["flaky"] == True:
                flakyFailedTests.append(tests["test_name"])
    return flakyFailedTests
print(get_flaky_failed_tests(test_runs))