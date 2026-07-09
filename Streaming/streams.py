import json

with open("streams.json", "r") as s:
    streams = json.load(s)

def get_completed_streams(streams):
    # Return a list of titles that have been completed
    titles = []
    for stream in streams: 
        if stream["completed"] == True: 
            titles.append(stream["title"])
    return titles
print(get_completed_streams(streams))

def group_by_platform(streams):
    # Group stream titles by platform
    # {"Disney+": ["The Mandalorian", ...], "Hulu": [...]}
    platform_titles = {}
    
    for stream in streams: 
        if stream["platform"] not in platform_titles:
            platform_titles[stream["platform"]] = []
        platform_titles[stream["platform"]].append(stream["title"])
    return platform_titles
print(group_by_platform(streams))
def get_longest_stream(streams):
    # Return the title of the stream with the highest duration_min
    duration = ""
    count = 0 
    for stream in streams: 
        time = stream["duration_min"]
        title = stream["title"]
        if time > count: 
            duration = title 
            count = time
    return duration
print(get_longest_stream(streams))
def get_average_rating_by_platform(streams):
    # Return average rating per platform
    # rounded to 2 decimal places
    rating_per_platform = {}
    count_rating = {}
    for stream in streams: 
        platform = stream["platform"]
        rating = stream["rating"]
        if platform not in rating_per_platform:
            rating_per_platform[platform] = 0
            count_rating[platform] = 0    
        rating_per_platform[platform] += rating
        count_rating[platform] += 1
    avg = {}
    for rate in rating_per_platform:
        avg[rate] = round(rating_per_platform[rate] / count_rating[rate], 2)
    return avg
print(get_average_rating_by_platform(streams))
def get_stream_summary(streams):
    # Return a list of strings summarizing each completed stream
    # Format: "The Mandalorian (Disney+): 45 min"
    # Only include completed streams
    formatted_stream = [f"{item['title']} ({item['platform']}): {item['duration_min']} min" for item in streams if item['completed']]
    
    return formatted_stream

print(get_stream_summary(streams))