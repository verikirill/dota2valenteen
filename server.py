from flask import Flask, render_template, redirect, request, abort, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/iloveyou')
def secon_page():
    return render_template('second_page.html')


if __name__ == '__main__':
    app.run(threaded=True)
