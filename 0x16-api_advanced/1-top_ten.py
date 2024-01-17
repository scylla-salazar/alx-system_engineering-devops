#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    # Reddit API URL for getting the hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent header to avoid potential issues
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Check if the subreddit exists
        if 'error' in data or 'data' not in data or 'children' not in data['data']:
            print("None")
            return

        # Print the titles of the first 10 hot posts
        for post in data['data']['children']:
            print(post['data']['title'])

    else:
        print("None")
