import json 

with open("saas.json", "r") as s:
    tickets = json.load(s)

def get_open_bugs(tickets):
    # Return a list of ticket IDs that are 
    # both open AND type "bug"
   open_ticket_ids_bugs = []
   for ticket in tickets: 
       status = ticket["status"]
       type = ticket["type"]
       if status == "open" and type == "bug":
           open_ticket_ids_bugs.append(ticket["ticket"])  
   return open_ticket_ids_bugs
print(get_open_bugs(tickets))

def group_tickets_by_assignee(tickets):
    # Group ticket IDs by assignee
    # {"Jordan": ["PROJ-101", "PROJ-103", "PROJ-107"], ...}
    assignee_name = {}
    ticket_id = []
    for ticket in tickets: 
       assignee = ticket["assignee"]
       ticket_name = ticket["ticket"]
       if assignee not in assignee_name:
           assignee_name[assignee] = []
       assignee_name[assignee].append(ticket_name)   
    return assignee_name
print(group_tickets_by_assignee(tickets))


def get_oldest_open_ticket(tickets):
    # Return the ticket ID of the open ticket 
    # with the most days_open
    ticket_most_days_open = ""
    count = 0 
    for ticket in tickets: 
        if count < ticket["days_open"]:
            ticket_most_days_open = ticket["ticket"]
            count += 1
    return ticket_most_days_open
print(get_oldest_open_ticket(tickets))

def get_average_days_open_by_priority(tickets):
    # Return average days_open per priority
    # across ALL tickets regardless of status
    # rounded to 2 decimal places
    all_tickets = {}
    ticket_priority = {}
    for ticket in tickets: 
        priority = ticket["priority"]
        days_open = ticket["days_open"]
        if priority not in ticket_priority:
            ticket_priority[priority] = 0
            all_tickets[priority] = 0
        all_tickets[priority] += days_open
        ticket_priority[priority] += 1
    
    avg = {}
    for num in all_tickets:
        avg[num] = round(all_tickets[num] / ticket_priority[num], 2)
    return avg
print(get_average_days_open_by_priority(tickets))

def get_critical_open_summary(tickets):
    # Return a list of strings for open critical tickets
    # Format: "PROJ-103 (Jordan) - 5 days open"
    formatted_critical_tickets = [f"{item['ticket']} ({item['assignee']}): {item['days_open']} days open" for item in tickets if item['priority'] == "critical" and item["status"] == "open"]
    
    return formatted_critical_tickets

print(get_critical_open_summary(tickets))