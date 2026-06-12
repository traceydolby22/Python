import json 

with open("customers.json", "r") as f:
    customers = json.load(f)


def get_churned_customer(customers):
    churned_customers = [] 
    # Return a list of names of churned customers
    for customer in customers: 
        if customer["status"] == "churned":
            churned_customers.append(customer["customer"])
    return churned_customers

#print(get_churned_customer(customers))

def get_revenue_by_city(customers):
    total_monthly_spent = {}

    for customer in customers: 
    # Return total monthly spend per city across ALL customers
    # {"Austin": 360, "Seattle": ..., "Chicago": ...}
        city = customer["city"]
        if city not in total_monthly_spent:
            total_monthly_spent[city] = 0 
        total_monthly_spent[city] += customer["monthly_spend"]
    return total_monthly_spent

#print(get_revenue_by_city(customers))

def get_longest_active_customer(customers):
    active_customer = "" 
    most_months_active = 0 
    for customer in customers: 
        if customer["status"] == "active":
            if customer["months_active"] > most_months_active:
                most_months_active = customer["months_active"]
                active_customer = customer["customer"]
    return active_customer
    # Return the name of the active customer 
    # with the most months_active

print( get_longest_active_customer(customers))

def get_plan_summary(customers):
    customer_per_plan = {}
    for customer in customers:
        plan = customer["plan"]
        if plan not in customer_per_plan:
            customer_per_plan[plan] = 0 
        customer_per_plan[plan] += 1
    return customer_per_plan


#print(get_plan_summary(customers))
    # Return count of customers per plan
    # {"premium": 4, "standard": 3, "basic": 3}