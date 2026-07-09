# Pattern 1 — Grouping into a dict of lists
#"Group X by Y" — like players by team, books by year
def get_books_by_year(books):
    result = {}
    for item in items:
        key = item["team"]
        if key not in result:
            result[key] = [] #The [] starts the list. The append adds to it every time. That's it.
        result[key].append(item["name"])
    return result

# Pattern 2 — Finding a single max/min value
#"Return the name of the player with the most/least X"
def get_player_with_most_points(players):
    best_value = 0
    best_name = ""
    for item in items:
        if item["points"] > best_value:
            best_value = item["points"] #= not +=. You're replacing, not accumulating.
            best_name = item["name"]
    return best_name

# Pattern 3 — Average by group
#"Return average X per Y"
def get_average_points_per_player(players):
    totals = {}
    counts = {}
    for item in items:
        key = item["position"]
        if key not in totals:
            totals[key] = 0
            counts[key] = 0
        totals[key] += item["value"]
        counts[key] += 1

    result = {}
    for key in totals:
        result[key] = round(totals[key] / counts[key], 2)
    return result
