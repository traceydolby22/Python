import json

with open("agents.json", "r") as f:
    agents = json.load(f)

def get_elite_agents(agents):
    elite_clearance = []
    #Get all active agents with clearance >= 8, sorted by missions_completed descending
    for agent in agents: 
        if agent["clearance"] >= 8 and agent["status"] == "active":
            elite_clearance.append(agent)
    sorted_agents = sorted(elite_clearance, key=lambda h: h["missions_completed"], reverse=True)
    elite_agents = [] 
    for agent in sorted_agents:
        elite_agents.append(agent["agent"])
    return elite_agents

def get_shared_skills(agents):
    shared_skills = {}
    shared = {}
    for agent in agents: 
        for skill in agent["skills"]: 
            if skill not in shared_skills:
                shared_skills[skill] = [] 
            shared_skills[skill].append(agent["agent"])
    for skill, agent_names in shared_skills.items():
        if len(agent_names) >= 2: 
            shared[skill] = agent_names
    return shared
   #Find which skills are shared by more than one agent
#    return: {"skill": [agent names who have it]}
#    only include skills with 2+ agents

def get_top_skill_agents(agents):
    agent_skill = {}
    for agent in agents: 
        if agent["status"] == "active":
            for skill in agent["skills"]:
                if skill not in agent_skill:
                    agent_skill[skill] = []         
                    agent_skill[skill] = agent["agent"] 
                else: 
                    for stored in agents: 
                        if stored["agent"] == agent_skill[skill]:
                            if agent["missions_completed"] > stored["missions_completed"]:
                                 agent_skill[skill] = agent["agent"] 
    return agent_skill

def get_readiness_report(agents):
    #Get a mission readiness report
    ready = [] 
     
    for agent in agents: 
        if agent["status"] == "active":
            if agent["clearance"] >= 7:
                if agent["missions_completed"] >= 20:
                    ready.append(agent["agent"])
        
    not_ready = []
    for agent in agents:
        if agent["status"] == "inactive" or agent["clearance"] < 7 or agent["missions_completed"] < 20:    
            not_ready.append(agent["agent"])

    total_active = 0
    for agent in agents: 
        if agent["status"] == "active":
            total_active += 1 
    return {
        "ready" : ready,
        "not_ready" : not_ready,
        "total_active" : total_active,
        "readiness_rate" : round(len(ready) / total_active * 100, 1)
    }

def group_by_clearace(agents):
    #Group agents by clearance level
    agent_clearance = {}
    for agent in agents: 
        level = agent["clearance"] 
        if level not in agent_clearance:
            agent_clearance[level] = [] 
        agent_clearance[level].append(agent["agent"])
    
    return agent_clearance
#    return: {9: ["Maya Chen", "Yuki Tanaka"], 10: [...], ...}
#    only include levels that have at least one agent


def get_mision_summary(agents):
    total_missions = 0 
    agent_missions_completed = [] 
    most_experienced = ""
    least_experienced = ""
    least_missions = float('inf') # means infinity, less fragile 
    most_missions = 0 
    for agent in agents: 
        agent_missions_completed.append(agent["missions_completed"])
        total_missions  = sum(agent_missions_completed)
    
    for agent in agents: 
        if agent["missions_completed"] > most_missions:
            most_missions = agent["missions_completed"] 
            most_experienced = agent["agent"]

    for agent in agents: 
        if agent["missions_completed"] < least_missions:
            least_missions = agent["missions_completed"]
            least_experienced = agent["agent"]
            
    return {
        "total_missions": total_missions,
        "average_missions" : round(total_missions/ len(agents), 1),
        "most_experienced" : most_experienced,
        "least_experienced" : least_experienced
    }

def get_status_summary(agents):
    agent_status_summary = {}
    for agent in agents: 
        status = agent["status"]
        if status not in agent_status_summary:
            agent_status_summary[status] = 0 
        agent_status_summary[status] += 1
    return agent_status_summary
    # Return a dict with each status and how many agents have it
    # return: {"active": 6, "inactive": 2, "suspended": 1}
print(get_mision_summary(agents))
print(get_status_summary(agents))

#print(get_top_skill_agents(agents))
#print(get_elite_agents(agents))
#print(get_shared_skills(agents))
#print(get_readiness_report(agents))
#print(group_by_clearace(agents))