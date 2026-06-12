import json

with open("missions.json", "r") as f:
    missions = json.load(f)

def get_failed_missions(missions):
    failed_missions = [] 
    #Get all failed missions, sorted by difficulty descending
    for mission in missions: 
        if mission["status"] == "failed":
            failed_missions.append(mission)
    sorted_missions = sorted(failed_missions, key=lambda h: h["difficulty"], reverse=True)
    
    return sorted_missions


def get_experienced_heroes(missions):
    #Get heroes who have been on at least 3 missions
    heroes_three_missions = {} 
    same_missions = {}
    for mission in missions: 
        for heroes in mission["team"]: 
            if heroes not in heroes_three_missions:
                heroes_three_missions[heroes] = 0
            heroes_three_missions[heroes] += 1
    
    for heroes, count in heroes_three_missions.items():
        if count >= 3:
            same_missions[heroes] = count
    return same_missions

def get_mission_counts(missions):
     # return: {"hero_name": mission_count} for heroes with 3+ missions
     return get_experienced_heroes(missions)

def get_overlapping_missions(missions):
    hero_overlap = {}
    # Find missions that share at least one team member
    for mission in missions: 
        hero_overlap[mission["mission"]] = []
        for other in missions: 
            if mission["mission"] != other["mission"]: 
                for hero in other["team"]:
                    if hero in mission["team"]:
                        hero_overlap[mission["mission"]].append(other["mission"]) 
                        break      
    return hero_overlap
 
#    return: {"mission_name": [other missions it shares a member with]}
   

print(get_failed_missions(missions))
print(get_experienced_heroes(missions))
print(get_mission_counts(missions))
print(get_overlapping_missions(missions))