#!/usr/bin/python3
"""
This module provides a function to query the Reddit API to fetch the hot
posts for a given subreddit and print the titles of the first 10 posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            'User-Agent': (
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) '
                'Gecko/20100101 Firefox/127.0'
                )
            }
    params = {
            'limit': 9
            }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", {})

            if not posts:
                print(None)
                return

            for post in posts:
                print(f"{i} {post["data"]["title"]}")

        else:
            print(None)
    except Exception as e:
        print(e)
        print(None)
