# 0x16. API Advanced

This project involves working with APIs, specifically the Reddit API, to practice querying endpoints, handling pagination, parsing JSON results, and implementing recursive functions. These tasks are common in technical interviews and can also be useful for personal projects.

## Learning Objectives

By the end of this project, you should be able to:

- Read API documentation to find the endpoints you're looking for.
- Use an API with pagination.
- Parse JSON results from an API.
- Make a recursive API call.
- Sort a dictionary by value.

## Project Requirements

- Use Python 3.4.3 for scripting.
- Organize imported libraries alphabetically.
- Ensure all files end with a new line.
- Follow PEP 8 style guidelines.
- Make all files executable.
- Provide documentation for all modules.
- Use the Requests module for HTTP requests to the Reddit API.

## Tasks

### Task 0: How many subs?

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, return 0.

### Task 1: Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. If the subreddit is invalid, print None.

### Task 2: Recurse it!

Write a recursive function that queries the Reddit API and returns a list of the titles of all hot articles for a given subreddit. If the subreddit is invalid, return None.

### Task 3: Count it!

Write a recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords. The count is case-insensitive and should sum duplicate keywords.

## Usage

To test your scripts, use the provided main files and run them with the appropriate arguments. For example:

```bash
$ python3 0-main.py programming
$ python3 1-main.py programming
$ python3 2-main.py programming
$ python3 100-main.py programming 'react python java javascript'
```

## Resources

- Reddit API Documentation
- Query String

## Author

- [Naoufalhdr] - [naoufalhadra96@gmail.com]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the ALX Software Engineering Program for providing this project.
- Inspiration from various online resources and tutorials on API usage.
