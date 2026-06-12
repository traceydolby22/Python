import json 

with open("pets.json", "r") as p:
    pets = json.load(p)

def group_pets_by_type(pets):
    # Return a dict grouping pet names by type
    # {"dog": ["Luna", "Rex", "Buddy"], "cat": [...]}
    pet_type = {}
    for pet in pets:
        type = pet["type"]
        if type not in pet_type:
            pet_type[type] = []
        pet_type[type].append(pet["name"])
    return pet_type
print(group_pets_by_type(pets))

def get_first_alphabetical_pet(pets):
    # Return the name of the pet that comes 
    # first alphabetically
    # Hint: "A" < "B" is valid in Python
    name_of_pet_alphabetical = ""
    for pet in pets:
        name = pet["name"]
        if name_of_pet_alphabetical == "" or name < name_of_pet_alphabetical:
            name_of_pet_alphabetical = name
        return name_of_pet_alphabetical    
print(get_first_alphabetical_pet(pets))
   
def get_average_age_by_type(pets):
    # Return average age per pet type
    # rounded to 2 decimal places
    # {"dog": 4.67, "cat": 5.0}
    pet_type = {} 
    pet_age = {} 
    for pet in pets: 
        type = pet["type"]
        age = pet["age"]
        if type not in pet_type:
            pet_type[type] = 0
            pet_age[type] = 0
        pet_type[type] += age
        pet_age[type] += 1
    
    result = {}
    for type in pet_type:
        result[type] = round(pet_type[type] / pet_age[type], 2)
    return result
    
print(get_average_age_by_type(pets))
        