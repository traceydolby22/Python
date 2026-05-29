import json
import urllib.request
import xml.etree.ElementTree as ET


with open("marvelCharacters.json", "r") as f:
    marvelCharacters = json.load(f)

# get the stats that are lower than 120 and add them to a list
def get_low_stat_heroes(heroes):
    heroes_list = [] 
    for hero in heroes:
        if hero["stats"] < 120: 
            heroes_list.append(hero)
    sorted_heroes = sorted(heroes_list, key=lambda h: h["stats"], reverse=True)
    names = [h["name"]for h in sorted_heroes]
    return names

# get the names of those that match super human strength print the list 
def get_super_strength_heroes(heroes):
    super_human_strength = []
    for hero in heroes: 
        if "super human strength" in hero["powers"]:
            super_human_strength.append(hero["name"])
    return super_human_strength

# Group heroes by power tier — "elite" (stats ≥ 150), 
# "mid" (120-149), "low" (under 120)
def get_heroes_by_power_tier(heroes):
    elite = []
    mid = []
    low = []
    for hero in heroes: 
        if hero["stats"] >= 150:
            elite.append(hero["name"])
        elif hero["stats"] >= 120:
            mid.append(hero["name"])
        else:
            low.append(hero["name"])
    return {
        "elite" : elite,
        "mid" : mid,
        "low" : low
    }

def get_heroes_with_shared_powers(heroes):
    sharing_powers = {}
    shared = {}
    for hero in heroes: 
        for power in hero["powers"]:
            if power not in sharing_powers:
                sharing_powers[power] = []
            sharing_powers[power].append(hero["name"])
    for power, names in sharing_powers.items():
        if len(names) > 1:
            shared[power] = names

    #shared = {power: names for power, names in sharing_powers.items() if len(names) > 1}
    return shared


print(get_heroes_with_shared_powers(marvelCharacters))
#print(get_low_stat_heroes(marvelCharacters))
#print(get_super_strength_heroes(marvelCharacters))
print(get_heroes_by_power_tier(marvelCharacters))
