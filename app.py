from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       username = request.form.get("uname")
       password = request.form.get("pwd")
       return "Your name is "+username + password
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)