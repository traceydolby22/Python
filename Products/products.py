import json

with open("products.json", "r") as p:
    products = json.load(p)

def group_product_by_category(products):
# Group available product names by category
    # Only include products with status "available"
    # {"Electronics": ["Wireless Headphones", ...], ...}
    category_to_add = {}
    for product in products:
        add_product = product["product"]
        category = product["category"]
        if product["status"] == "available":
            if category not in category_to_add:
                category_to_add[category] = []
            category_to_add[category].append(add_product)
    return category_to_add
print(group_product_by_category(products))

def get_most_expensive_product(products):
    expensive_good = ""
    price_of_good = 0 
# Return the name of the most expensive 
    # available product
    for product in products:
        add_product = product["product"]
        if product["status"] == "available":
            if add_product not in expensive_good:
                if price_of_good < product["price"]:   
                    expensive_good = add_product
                    price_of_good = product["price"]

    return expensive_good
print(get_most_expensive_product(products))

def get_avg_price_per_category(products):
# Return average price per category
    # across ALL products regardless of status
    # rounded to 2 decimal places
    all_product_list = {}
    total_price = {} 
    for product in products: 
        add_category = product["category"]
        add_price = product["price"]
        if add_category not in all_product_list:
            all_product_list[add_category] = 0
            total_price[add_category] = 0
        all_product_list[add_category] += add_price
        total_price[add_category] += 1
    average = {}
    for total in all_product_list:
        average[total] = round(all_product_list[total]/ total_price[total], 2)
    return average
print(get_avg_price_per_category(products))