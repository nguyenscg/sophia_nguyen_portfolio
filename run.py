from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello! This is the name page <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()