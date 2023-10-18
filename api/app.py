from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("index.html")

@app.route("/shop", methods=["POST"])
def shop_page():
    input_name = request.form.get("name")
    input_color = request.form.get("color")

    return render_template("main_shop.html", name=input_name, color=input_color)

@app.route("/checkout", methods=["POST"])
def checkout():
    
    input_name = request.form.get("name")
    input_color = request.form.get("color")

    input_item = request.form.get("item")
    input_quantity = request.form.get('quantity')

    return render_template("checkout.html", name=input_name, color=input_color, item=input_item, quantity=input_quantity)