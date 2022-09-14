from operator import index
from os import abort
from queue import Empty
from urllib import request
from flask import Flask, render_template, request
from inc.indexing import indexURL

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def process():
    if request.method == "POST":
        url = request.form.get('index')
        # let's see
        return indexURL(url)



if __name__ == "__main__":
    app.run()