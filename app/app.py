from flask import Flask, redirect, render_template, request, session, url_for, Response, send_file
import os
import io

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def home():
    '''route to the homepage'''
    return render_template("index.html")

def retrieve_classes():
    '''return a list of class objects'''

@app.route('/<path:path>')
def catch_all(path):
    '''catch errors and redirect to home page'''
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)

