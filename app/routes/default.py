from .. import app
from flask import render_template, url_for

products = [
    {"name" : "pizza", "price" : 20.6326873474832},
    {"name" : "sandwich", "price" : 10.6372642548639},
    {"name" : "cola", "price" : 6.69678756875489}
]
@app.template_filter("format_round")
def format_round(price: float):
    return f"{price:.3f} ₮"
    

    
@app.route("/")
def index():
    return render_template("_base.html", products=products)

@app.route("/product/<name>")
def details(name):
    for i in products:
        if i['name'] == name:
            return render_template("product_details.html", product = i, format_round=format_round, products=products)