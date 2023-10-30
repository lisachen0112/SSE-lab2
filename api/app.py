import re
import numpy as np
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


def square_cube(nums):
    for i in nums:
        if (np.sqrt(i) % 1 == 0) and (np.cbtr(i) % 1 == 0):
            return str(i)


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

    elif "square and cube" in query:
        return square_cube(get_list_of_number(query))

    else:
        return "Query received"


@app.route("/query", methods=["GET"])
def query_handler():

    query = request.args.get('q')

    return process_query(query)
