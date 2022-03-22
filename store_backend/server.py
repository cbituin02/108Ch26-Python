from flask import Flask

app = Flask("server")

@app.route("/")
def home():
    return "Hello from Flask"




@app.route("/me")
def about_me():
    return "Caleb Bituin"


app.run(debug=True)     