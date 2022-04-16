import json
from flask import Flask, abort, request
from mock_data import catalog
from config import db
from bson import ObjectId


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

    products = []
    cursor = db.products.find({})  # curosr is collection

    for prod in cursor:
        prod["_id"] = str(prod["_id"])  # fix _id
        products.append(prod)

    return json.dumps(products)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()  # return data (payload) from the request

    db.products.insert_one(product)
    print(product)

# fix _id
    product["_id"] = str(product["_id"])


# crash
    return json.dumps(product)


# GET /api/catalog/count -> how many products exist in the catalog
@app.route("/api/catalog/count")
def product_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1

    #  cnt - len(list(cursor))

    return json.dumps(count)


# get /api/catalog/total -> the sum of all the product's prices
@app.route("/api/catalog/total")
def catalogt_total():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)

#  /api/product/PATRICK


@app.route("/api/product/<id>")
def get_by_id(id):

    prod = db.products.find_one({"_id": ObjectId(id)})

    if not prod:
        # not found, return an error 404
        return abort(404, "no product with such id")

    prod["_id"] = str(prod["_id"])
    return json.dumps(prod)


# should return the product with the lowest price
@app.route("/api/product/cheapest")
def cheapest_product():

    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)


# get /api/categories
# should return list of strings representing the unique categories

@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)

    return json.dumps(categories)


@app.get("/api/catalog/<category>")
def prods_by_category(category):

    products = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(products)


@app.get("/api/someNumbers")
def some_numbers():
    # return a list with numbers from 1 to 50 as json
    numbers = []
    for num in range(1, 51):
        numbers.append(num)

    return json.dumps(numbers)


#############################################################
################## Coupon Code EndpPonts ####################
#############################################################
allCoupons = []

# create the GEt /api/couponCode
# return all coupons as json list


@app.route("/api/couponCode", methods=["GET"])
def get_coupons():
    return json.dumps(allCoupons)

# create the Post    /api/couponCode
# get the coupon fom the request
# assign an _id
# and add it to all coupons
# return the coupon as json


@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
    coupon = request.get_json()
    coupon["_id"] = 42

    allCoupons.append(coupon)

    return json.dumps(coupon)


app.run(debug=True)
