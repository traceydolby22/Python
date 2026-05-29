campaigns = [
    {"id": 1,   "title": "Summer iOS Push",  "target_audience": "ios",     "budget": 5000},
    {"id": 2,   "title": "",                 "target_audience": "ios",     "budget": 3000},
    {"id": 3,   "title": "MacOS Holiday",    "target_audience": "macos",   "budget": 0},
    {"id": 4,   "title": "Web Retargeting",  "target_audience": "web",     "budget": 8000},
    {"id": "x", "title": "Bad ID Camp",      "target_audience": "ios",     "budget": 1000},
    {"id": 5,   "title": "Unknown Platform", "target_audience": "android", "budget": 2000},
    {"id": 6,   "title": "Back to School",   "target_audience": "web",     "budget": 4500},
]

VALID_AUDIENCES = ["ios", "macos", "web"]

def is_valid_campaign(campaign):
    # one dict — check: id is int, title non-empty,
    if not isinstance(campaign["id"],int) :
       return False
    if len(campaign["title"]) == 0 :
        return False
    if campaign["target_audience"] not in VALID_AUDIENCES:
        return False
    if campaign["budget"] <= 0: 
        return False 
    return True
    # target_audience in VALID_AUDIENCES, budget > 0
    
def validate_all(campaigns):
    # whole list — loop inside
    valid_titles = []
    invalid_titles = []
    valid = 0 
    for campaign in campaigns: 
        if is_valid_campaign(campaign) != True:
            invalid_titles.append(campaign["title"])
        else: 
            valid_titles.append(campaign["title"])
            valid += 1 
    return {
            "valid" : valid_titles,
            "invalid" : invalid_titles,
            "total" : len(campaigns),
            "pass_rate" : round(valid / len(campaigns) * 100, 1)
    }
    # return a dict with:
    # "valid"     → list of valid campaign titles
    # "invalid"   → list of invalid campaign titles
    # "total"     → total number of campaigns
    # "pass_rate" → percentage valid, rounded to 1 decimal

report = validate_all(campaigns)
# print the full report
print(f"Total:  {report["total"]}")
print(f"Pass rate:  {report["pass_rate"]}%")
print(f"\n√ Valid:  ({len(report["valid"])}:")
for title in report["valid"]:
    print(f"  - {title}")
print(f"\nx Invalid:  ({len(report["invalid"])}:")
for titls in report["invalid"]:
    print(f"  - {title}")

