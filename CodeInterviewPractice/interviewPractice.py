
def duplicate_nums(num):
    dupes = {}
    count = []

    for number in num:
        if number not in dupes:
            dupes[number] = 0
        dupes[number] += 1
    for dupe in dupes:
        if dupes[dupe] > 1:
            count.append(dupe)
    return count

num = [1, 2, 2, 3, 4, 4, 4, 5]
#print(duplicate_nums(num))

#Problem 1 — array transformation (the exact category Disney candidates described):
#Given a list of integers, return a new list where every number is doubled, but skip any negative numbers entirely.
def doubled_numbers(num):
    doubled_list = []
    for number in num:
        if number > 0:
            doubled = number * 2
            doubled_list.append(doubled)
    return doubled_list
#print(doubled_numbers([1, -2, 3, 4, -5])) # → [2, 6, 8]

#Problem 2 — string manipulation:
#Given a string, return the number of vowels it contains (a, e, i, o, u — case insensitive).
def vowels(letters):
    letter = []
    count = 0 
    for vowel in letters: 
        if vowel.lower() in "aeiou":
            letter.append(vowel)
            count += 1
    return count
#print(vowels("Hello World")) # → 3

#Problem 3 — the two-phase pattern you just discovered tonight, applied fresh:
#Given a list of words, return only the words that appear exactly once in the list (true uniqueness, not "at least once").
def unique_words(words):
    only_once = {}
    count = 0 
    unique = []
    for word in words:
        if word not in only_once:
            only_once[word] = 0 
        only_once[word] += 1
    for word in only_once:
        if only_once[word] == 1: 
            unique.append(word)
    return unique
#print(unique_words(["cat", "dog", "cat", "bird", "dog", "fish"])) #→ ["bird", "fish"]

#Problem 4 — combining array + condition, QA-flavored:
#Given a list of test run durations in seconds, return how many runs took longer than 5 seconds.
def longer_than_five_seconds(tests):
    runs = []
    for test in tests: 
        if test > 5: 
            runs.append(test)
    return len(runs)
#print(longer_than_five_seconds([3.2, 7.1, 4.8, 9.0, 2.1, 6.5])) # → 3

#Problem 1:
#Given a list of test results like ["pass", "fail", "pass", "pass", "fail"], return the percentage of tests that passed, rounded to 1 decimal place.
def percentage_passed(results):
    passed_tests = 0
    
    for result in results: 
        if result == "pass":
            passed_tests += 1 
    percentage = round(passed_tests / len(results)*100, 1)  
    return percentage
    
test_results = ["pass", "fail", "pass", "pass", "pass", "fail"]
print(percentage_passed(test_results))

#Problem 2:
#Given two lists of build numbers — one from a nightly run, one from a weekly run — return a list of build numbers that appear in BOTH lists.
#[101, 102, 103] and [102, 103, 104] → [102, 103]
def build_numbers(nightly, weekly):
    nightly_and_weekley_run = {}
    for build in nightly: 
        nightly_and_weekley_run[build] = 0
        
    for build in weekly:
        if build in nightly_and_weekley_run:
            nightly_and_weekley_run[build] +=1
        if build not in nightly_and_weekley_run:
            nightly_and_weekley_run[build] = 0
    builds_in_both = []
    for build in nightly_and_weekley_run:
        if nightly_and_weekley_run[build] == 1:
            builds_in_both.append(build)
    return builds_in_both
nightly_runs = [101, 102, 103] 
weekly_runs = [102, 103, 104, 105]
print(build_numbers(nightly_runs, weekly_runs))       

#Problem 3:
#Given a string representing a test name like "test_login_with_valid_credentials", write a function that converts it into a readable sentence: 
# "Test login with valid credentials" (capitalize first letter, replace underscores with spaces).

def readable_test_name(test_names): 
    new_string = test_names.replace( "_" , " ").capitalize()  
    return new_string
         
print(readable_test_name("test_login_with_valid_credentials"))