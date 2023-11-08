import re
import numpy as np
import requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def login_page():
    return render_template("index.html")


@app.route("/shop", methods=["POST"])
def shop_page():
    input_name = request.form.get("name")
    input_color = request.form.get("color")

    return render_template("main_shop.html",
                           name=input_name, color=input_color)


@app.route("/checkout", methods=["POST"])
def checkout():

    input_name = request.form.get("name")
    input_color = request.form.get("color")

    input_item = request.form.get("item")
    input_quantity = request.form.get('quantity')

    return render_template("checkout.html",
                           name=input_name, color=input_color,
                           item=input_item, quantity=input_quantity)


@app.route("/github_api")
def github_api():
    return render_template("github_api.html")


@app.route("/user_info", methods=["POST"])
def user_info():

    username = request.form.get("github-username")
    data = gather_data(username)
    
    return render_template("user_info.html", username=username, data=data)


# Function to gather a list of publically accessible repos of a given user
def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()


# Gathers the lastest commit data for a given repo
def get_latest_commit(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            return commits[0]  # Return the latest commit
    return None


# Gather data for all repos of a given user
def gather_data(username):
    data = []
    with requests.Session() as session:  # Use a Session for connection pooling
        for repo in get_repos(username):
            repo_data = {
                "repo_name": repo["name"],
                "last_update": repo["updated_at"],
                "last_push": repo["pushed_at"]
            }

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


def get_list_of_number(query):
    return [int(i) for i in re.findall(r'[0-9]+', query)]


def largest(nums):
    return str(max(nums))


def smallest(nums):
    return str(min(nums))


def addition(nums):
    return str(sum(nums))


def product(nums):
    return str(np.prod(nums))


def is_cube(n):
    cube_root = n**(1./3.)
    return round(cube_root) ** 3 == n


def is_square(n):
    cube_root = n**(1./2.)
    return round(cube_root) ** 2 == n


def square_cube(nums):
    for i in nums:
        if (is_cube(i)) and (is_square(i)):
            return str(i)


def is_prime(num):
    state = True
    if num <= 0:
        state = False
        return state
    else:
        for i in range(2, num):
            if num % i == 0:
                state = False
                break
        return state


def prime(nums):
    for num in nums:
        if is_prime(num):
            return str(num)


def subtraction(nums):
    return str(nums[0] - nums[1])


def process_query(query):

    # if query == "dinosaurs":
    #     return "Dinosaurs ruled the Earth 200 million years ago"
    # elif query == 'asteroids':
    #     return "Unknown"

    if "plus" in query:
        print(addition(get_list_of_number(query)))
        return addition(get_list_of_number(query))

    elif "largest" in query:
        return largest(get_list_of_number(query))

    elif "multiplied" in query:
        return product(get_list_of_number(query))

    elif "square and a cube" in query:
        return square_cube(get_list_of_number(query))

    elif "prime" in query:
        return prime(get_list_of_number(query))

    elif "minus" in query:
        return subtraction(get_list_of_number(query))
    else:
        return "Query received"


@app.route("/query", methods=["GET"])
def query_handler():

    query = request.args.get('q')

    return process_query(query)
