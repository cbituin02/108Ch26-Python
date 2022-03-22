

def test_dict():
    me = {
        "first": "Caleb",
        "last": "Bituin",
        "age": 35,
        "hobbies": [],
        "address": {
            "street": "Sesame",
            "city": "Quohog"
        }
    }


    print(me["first"] + " " + me["last"])

    print(f"My age is: {me['age']}")

    print(me["address"]["street"])

    # add new keys
    me["color"] = "red"

    # modify existing keys
    me["age"] = 36

    # check if a key exist in a dict
    if "age" in me:
        print("Age exist")

print("---- Dictionary Test ----")
test_dict()