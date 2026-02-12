from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/servics")
def Services():
    return render_template("Services.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/about")
def about():
    return render_template("About.html")
app.run(debug=True)