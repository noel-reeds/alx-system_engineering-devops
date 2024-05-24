#!/usr/bin/python3
"""show number of subs"""
import requests
import sys


def number_of_subscribers(subreddit):
    # oauth 2.0 parameters
    client_id = 'M0L9-1g6atSv0wa1HgmsmQ'
    client_secret = 'nmFkMT-JZb9IULYpO9J31ePFNqasyw'
    redirect_uri = 'http://localhost:8080'
    username = 'noel-reeds'
    password = '2Pq-bTe*fqPRsSq'
    token_uri = "https://oauth.reddit.com/api/v1/access_token"
    scope = "read"

    # request authorization
    params = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    headers = {
        "User-Agent": "MyAPI/0.0.1"
    }
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    res = requests.post(token_uri, data=params, auth=auth, headers=headers)
    response = res.json()
    access_token = response.get("access_token")
    if access_token:
        headers = {
            "Authorization": f"bearer {access_token}",
            "User-Agent": "MyAPI/0.0.1"
        }
        endpoint = f"https://oauth.reddit.com/r/{subreddit}/about.json"
        subreddit_info = requests.get(endpoint, headers=headers)
        if subreddit_info.status_code == 200:
            subreddit_info = subreddit_info.json()
            subscribers = subreddit_info["data"]["subscribers"]
            return subscribers
        else:
            return 0
