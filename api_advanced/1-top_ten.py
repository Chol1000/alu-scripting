#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    
    # Make the GET request to the Reddit API
    RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

    # Check if the subreddit exists
    if RESPONSE.status_code == 404:
        print(None)  # Non-existent subreddit
        return
    elif RESPONSE.status_code != 200:
        print(None)  # For any other error
        return

    # Parse the JSON response and print hot post titles
    HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
    for post in HOT_POSTS:
        print(post.get('data').get('title'))

