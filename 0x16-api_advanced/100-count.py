#!/usr/bin/python3
"""
Implement the recursive function that queries the Reddit API, parses
the titles of all hot articles, and prints a sorted count of
given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot
    articles, and prints a sorted count of given keywords
    (case-insensitive).
    """
    if not counts:
        word_list = [word.lower() for word in word_list]
        counts = {word: 0 for word in word_list}

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
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post["data"]["title"].lower().split()
            for word in word_list:
                counts[word] += title.count(word)

        after = data.get("data", {}).get("after", None)
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(),
                                   key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    except Exception as e:
        pass
