import json
from flask import Flask, abort
from mock_data import catalog


app = Flask("server")


@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Caleb Bituin"


#########################################################
################### API ENDPOINTS #######################
###################  RETURN JSON  #######################
#########################################################


@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)


@app.route("/api/catalog", methods=["post"])
def save_product():
    pass

# GET /api/catalog/cpunt -> how many products exist in the catalog
@app.route("/api/catalog/count", methods=["get"])
def product_count():
    return json.dumps(len(catalog))


# get /api/catalog/total -> the sum of all the product's prices
@app.route("/api/catalog/total")
def catalogt_total():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)

#  /api/product/PATRICK
@app.route("/api/product/<id>")
def get_by_id(id):
    # find the product with _id is eqaul to id
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return abort(404, "no product with such id")

app.run(debug=True)