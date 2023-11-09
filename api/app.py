from flask import Flask, render_template, request
from api.utils.maths_utils import *
from api.utils.github_api_utils import *
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
    # print(data)
    
    return render_template("user_info.html", username=username, data=data)


@app.route("/repository_search", methods=["POST"])
def search_results():

    search = request.form.get("search")
    data = get_search_results(search)

    return render_template("repositories_search.html", search=search, data=data)


def process_query(query):

    # if query == "dinosaurs":
    #     return "Dinosaurs ruled the Earth 200 million years ago"
    # elif query == 'asteroids':
    #     return "Unknown"

    if "plus" in query:
        # print(addition(get_list_of_number(query)))
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
