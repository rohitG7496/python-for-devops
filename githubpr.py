import requests

# 1. Fetching the data from GitHub API
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details = response.json()

# 2. Creating an empty dictionary to store our counts
pr_counts = {}

# 3. Looping through the PR data
for i in range(len(details)):
    username = details[i]["user"]["login"]
    
    # 4. Using the safe .get() method we discussed earlier!
    # If the username isn't in the dict, it returns 0. Then we add 1.
    pr_counts[username] = pr_counts.get(username, 0) + 1

# 5. Printing the final results nicely
print("--- PR Counts Per User ---")
for user, count in pr_counts.items():
    print(f"User: {user} | Pull Requests: {count}")