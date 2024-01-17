#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful (status code 200) and if the subreddit exists
    if response.status_code == 200:
        try:
            results = response.json()["data"]["children"]
            for post in results:
                print(post["data"]["title"])
        except KeyError:
            print("None")
    else:
        print("None")
