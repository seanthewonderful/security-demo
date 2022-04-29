from flask import Flask, render_template, url_for
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/69c3d67fee24ce6ca0d5")
posts = response.json()


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def post(id):
    # for post in posts:
    #     if post['id'] == id:
    #         print(post)
    return render_template("post.html", posts=posts, id=id)




if __name__ == "__main__":
    app.run(debug=True)