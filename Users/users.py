import json

with open("users.json", "r") as u:
    users = json.load(u)

def get_incomplete_sessions(users):
    # Return list of usernames who did NOT complete their UAT session
    usersNotCompleted = []
    for user in users:
        if user["completed"] == False:
            usersNotCompleted.append(user["user"])
    return usersNotCompleted


def group_feedback_by_feature(users):
    # Group feedback strings by feature
    # {"checkout_redesign": ["Smooth experience...", ...], ...}
    featureToAdd = {}
    for user in users:
        feature = user["feature"]
        feedback = user["feedback"]
        if feature not in featureToAdd:
            featureToAdd[feature] = []
        featureToAdd[feature].append(feedback)
    return featureToAdd


def get_lowest_rated_session(users):
    # Return the username of the session with the LOWEST rating
    lowestRating = float('inf')
    userWithLowestRating = ""
    for user in users: 
        rating = user["rating"]
        username = user["user"]
        if lowestRating > rating:
            lowestRating = rating
            userWithLowestRating = username
    return userWithLowestRating

def get_average_rating_by_feature(users):
    # Return average rating per feature, rounded to 2 decimal places
    ratingPerFeature = {}
    featureToAdd = {}
    count = {}
    for user in users: 
        feature = user["feature"]
        rating = user["rating"]
        if feature not in featureToAdd:
            featureToAdd[feature] = 0 
            count[feature] = 0
        featureToAdd[feature] += rating
        count[feature] += 1
    print(featureToAdd)
    for average in featureToAdd:
        ratingPerFeature[average] = round(featureToAdd[average]/ count[average], 2)
    return ratingPerFeature


def get_critical_issues(users):
    # Return usernames where completed is False AND rating is 2 or lower
    # This simulates flagging the most severe UAT failures for immediate triage 
    userNotCompleteRatedLow = []
    for user in users: 
        if user["completed"] == False:
            if user["rating"] <= 2:
                userNotCompleteRatedLow.append(user["user"])
    return userNotCompleteRatedLow
