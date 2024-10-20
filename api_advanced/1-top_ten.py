#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
    
    # Check if the subreddit exists
    if RESPONSE.status_code == 404:
        print(None)
        return
    elif RESPONSE.status_code != 200:
        print(None)
        return

    # Parse the JSON response and print hot post titles
    HOT_POSTS = RESPONSE.json().get("data", {}).get("children", [])
    for post in HOT_POSTS:
        print(post.get('data').get('title'))

