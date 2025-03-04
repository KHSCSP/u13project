import json, requests

# what type of data does this return?
# how many items?
# what type of data is each item?
def get_activities(num):
    data = []
    url = 'https://bored.api.lewagon.com/api/activity'
    for i in range(num):
        data.append(requests.get(url).json())
    return data


# what type of data does this return?
# how many items?
# what type of data is each item?
def get_memes():
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    return response.json().get('data').get('memes')