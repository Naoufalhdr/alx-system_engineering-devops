#!/usr/bin/python3
"""
This module create a recursive function that queries the Reddit API and
fetches all the hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing the
    titles of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) '
            'Gecko/20100101 Firefox/127.0'
        )
    }
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            if not posts:
                return hot_list if hot_list else None

            for post in posts:
                hot_list.append(post["data"]["title"])

            after = data.get("data", {}).get("after", None)
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
