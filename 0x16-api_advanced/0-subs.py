#!/usr/bin/python3
""" This module provides a function to query the Reddit API and return
the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API to find the number of subscribers for a given
    subreddit."""

    # Define the URL and set a custom User-Agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            'User-Agent': (
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) '
                'Gecko/20100101 Firefox/127.0'
                )
            }

    # Make the request & response and exception handling
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
