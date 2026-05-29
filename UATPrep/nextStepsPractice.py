# Scenario: You're validating mobile devices before running an automated test suite. 
# Only devices that are active, running a supported OS, and have enough battery should be included in the test run.
# Pattern: Function takes one dict → multiple if checks → return True/False. Loop outside

SUPPORTED_VERSIONS = ["iOS 16", "iOS 17", "iOS 18"]

devices = [
    {"name": "iPhone 14",    "status": "active",   "os_version": "iOS 17", "battery_level": 85},
    {"name": "iPhone 12",    "status": "inactive", "os_version": "iOS 16", "battery_level": 90},
    {"name": "iPhone 15",    "status": "active",   "os_version": "iOS 18", "battery_level": 15},
    {"name": "iPhone 11",    "status": "active",   "os_version": "iOS 15", "battery_level": 75},
    {"name": "iPhone 13",    "status": "active",   "os_version": "iOS 17", "battery_level": 60},
]


def is_ready(device):
    if device["status"] != "active":
        return False
    if device["os_version"]not in SUPPORTED_VERSIONS: 
        return False
    if device["battery_level"] < 20:
        return False
    return True
list_not_ready = [] 
# loop, print name + result
for device in devices: 
    #print(f"{device['name']}, {is_ready(device)}")
    if is_ready(device) == False:
        list_not_ready.append(device["name"])
#print(list_not_ready)
# bonus: collect and print not-ready device names


# Scenario: End of sprint. Write a function that takes 
# the full list of bugs filed this sprint and returns a summary report — total bugs, 
# how many are open vs resolved, and which ones are still open.

# Pattern Function takes a list → loops inside → returns a dict with mixed values (numbers AND a list). Print numbers directly, loop over the list.

bugs = [
    {"title": "Payment timeout",      "severity": "high",   "status": "open"},
    {"title": "Login button missing", "severity": "high",   "status": "resolved"},
    {"title": "Slow load time",       "severity": "medium", "status": "open"},
    {"title": "Campaign not sending", "severity": "high",   "status": "open"},
    {"title": "Typo in footer",       "severity": "low",    "status": "resolved"},
    {"title": "API returns 500",      "severity": "high",   "status": "open"},
]

def get_bug_report(bugs):
    # loop inside
    total_open  = 0 
    total_closed = 0
    open_titles = []
    for bug in bugs: 
        if bug["status"] == "open":
            total_open += 1 
            open_titles.append(bug["title"])    
        else: 
            total_closed += 1
    # return dict with: total, open_count, resolved_count, open_titles
    return {
        "total" : len(bugs),
        "open_count" : total_open,
        "resolved_count" : total_closed,
        "open_titles" : open_titles
    } 

# print total, open_count, resolved_count directly
report = get_bug_report(bugs)
#print(f"Total:  {report['total']} ")
#print(f"Open:  {report['open_count']} ")
#print(f"Open:  {report['resolved_count']} ")

# loop over open_titles and print each one
#print(f"\nStill open ({report["open_count"]}): ")
##for title in report["open_titles"]:
   # print(f"  - {title}")
    
# Scenario: You're validating push notification 
# payloads before they go out to iOS devices. A bad payload reaching 
# 40 million devices is a P0 incident. Validate each one carefully.

# Pattern Same as Ex 3 from the last set — check if keys exist before accessing them. One dict, no loop inside the function.
payloads = [
    {"message": "Summer sale is live!",  "recipient_count": 5000,  "campaign_id": 101},
    {"message": "",                      "recipient_count": 3000,  "campaign_id": 102},
    {"message": "Holiday deals await",   "recipient_count": -1,    "campaign_id": 103},
    {"message": "Back to school",        "recipient_count": 8000,  "campaign_id": 104},
    {"recipient_count": 2000,            "campaign_id": 105},
    {"message": "Flash sale ends soon",  "recipient_count": 10000},
]

def is_valid_payload(payload):
    # returns True if: "message" key exists and is a non-empty string,
    if "message" not in payload:
        return False
    if len(payload["message"]) == 0:
        return False
     # "recipient_count" key exists and is an int greater than 0, 
    if "recipient_count" not in payload: 
        return False
    if payload["recipient_count"] <= 0: 
        return False
    # "campaign_id" key exists and is an int.
    if "campaign_id" not in payload: 
        return False
    if not isinstance(payload["campaign_id"], int):
        return False 
    return True
    
for i, payload in enumerate(payloads, start = 1):
    print(f"Payload {i}: {is_valid_payload(payload)}")
    
# Scenario: You're running a full validation pass on test environments before a release. Each environment needs to be active, 
# have the right version deployed, and have passing health checks. Write both functions and print a complete report.


APPROVED_VERSIONS = ["v2.1", "v2.2", "v2.3"]

environments = [
    {"name": "prod-us-east",  "status": "active",   "version": "v2.3", "health_check": "passing"},
    {"name": "prod-us-west",  "status": "active",   "version": "v2.1", "health_check": "failing"},
    {"name": "staging",       "status": "active",   "version": "v2.3", "health_check": "passing"},
    {"name": "prod-eu",       "status": "inactive", "version": "v2.2", "health_check": "passing"},
    {"name": "prod-apac",     "status": "active",   "version": "v2.0", "health_check": "passing"},
    {"name": "qa-env",        "status": "active",   "version": "v2.2", "health_check": "passing"},
]

def is_ready_for_release(env):
    # one dict, returns True if: status is "active"
    if env["status"] != "active":
        return False
    # version is in APPROVED_VERSIONS,
    if env["version"] not in APPROVED_VERSIONS:
        return False
    # health_check is "passing"
    if env["health_check"] != "passing":
        return False
    return True

def get_release_report(environment):
    ready = [] 
    not_ready = [] 
    # whole list, loops inside, 
    for env in environment: 
        if is_ready_for_release(env): # is the same as if is_ready_for_release(env) == True:
            ready.append(env["name"])
        else: 
            not_ready.append(env["name"])
# returns dict with: ready (list of names), not_ready (list of names), total, ready_count, not_ready_count.
    return {
        "ready" : ready,
        "not_ready" : not_ready,
        "total" : len(environment),
    }
#Printing guide for this one: ready_count and not_ready_count → print directly. ready and not_ready lists → loop over each. 
# Try writing the print section yourself before looking at the solution.
report = get_release_report(environments)
# print the full report here
print(f"{report}")
# numbers → directly
print(f" Ready - {len(report["ready"])}, Not Ready - {len(report["not_ready"])}, Total - {report["total"]}")
# lists → with loops
for name in report["ready"]: 
    print(f"  - {name} ")
for name in report["not_ready"]:
    print(f" - {name}")