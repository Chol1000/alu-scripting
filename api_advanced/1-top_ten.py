#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit.

This module fetches the top 10 hot posts from a specified subreddit
using the Reddit API and prints their titles. If the subreddit does not
exist or has no posts, it prints 'None'.
"""

import requests


def top_ten(subreddit):
    """Fetches and prints the titles of the top 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Outputs:
        Titles of the top 10 hot posts if the subreddit exists, otherwise 'None'.
    """
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Check if subreddit exists
        if RESPONSE.status_code == 404:
            print("None")
            return

        # Check if the response was successful
        RESPONSE.raise_for_status()

        HOT_POSTS = RESPONSE.json().get("data").get("children")

        if not HOT_POSTS:
            print("None")
            return

        for post in HOT_POSTS:
            print(post.get('data').get('title'))

    except Exception:
        print("None")


# Example usage
if __name__ == "__main__":
    top_ten(subreddit)

