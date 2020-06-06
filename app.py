import time

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts", methods=["POST"])
def posts():

    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response.
    time.sleep(1)

    # Return list of posts.
    return jsonify(data)

if __name__ == "__main__":
    app.run()


#
# from flask import Flask, render_template, request, session
# #from flask_session import Session
#
# app = Flask(__name__)
#
# #app.config["SESSION_PERMANENT"] = False
# #app.config["SESSION_TYPE"] == "filesystem"
# #Session(app)
#
# notes = [1]
#
# @app.route("/", methods = ["GET", "POST"])
# def index():
#     if request.method == "POST":
#         note = request.form.get("note")
#         notes.append(note)
#
#     return render_template("index.html", notes = notes)
#
#
#
# if __name__ == '__main__':
#     app.run()
