import requests


# Function to gather a list of publicly accessible repos of a given user
def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


# Gathers the latest commit data for a given repo
def get_latest_commit(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            return commits[0]
    return None


# Gather data for all repos of a given user
def gather_data(username):
    repos = get_repos(username)  # Get the list of repositories
    data = []
    if repos:
        for repo in repos:
            repo_data = {
                "repo_name": repo["name"],
                "last_update": repo["updated_at"],
                "last_push": repo["pushed_at"]
            }

            # Update each repository with additional commit data
            latest_commit = get_latest_commit(username, repo["name"])
            if latest_commit:
                repo_data.update({
                    "commit_hash": latest_commit["sha"],
                    "commit_author": latest_commit["commit"]["author"]["name"],
                    "commit_date": latest_commit["commit"]["author"]["date"],
                    "commit_message": latest_commit["commit"]["message"]
                })

            data.append(repo_data)
    return data

def get_search_results(search):
    url = f"https://api.github.com/search/repositories?q={search}&sort=stars&per_page=10"
    response = requests.get(url)

    if response.status_code == 200:
        response_data = response.json()
        data = []        
        for item in response_data['items']:
            repo_data = {
                "Repository name": item['name'],
                "Description": item['description'],
                "Stars": item['stargazers_count'],
                "Created at": item['created_at'],
                "url": item['html_url']
            }
            data.append(repo_data)

    return data

