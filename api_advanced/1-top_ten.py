#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        
        # Debugging: Print JSON keys
        print(json_data.keys())

        data = json_data.get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for i in range(min(10, len(children))):
                    title = children[i].get('data').get('title')
                    if title is not None:
                        print(title)
                    else:
                        print("Title not found")
            else:
                print("No children found in JSON data")
        else:
            print("No data found in JSON response")
    else:
        print(None)


# Example call to the function
top_ten('python')
