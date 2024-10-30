from flask import Flask, request, render_template
from datetime import datetime
from pymongo import MongoClient

def create_app():

    app = Flask(__name__)
    client = MongoClient("mongodb+srv://marlonmontenegropaz:Montenegro12@datahive.fzhuskp.mongodb.net/")
    app.db = client.MicroBlog

    @app.route("/", methods=["GET", "POST"])
    def home():

        if request.method == "POST":
            entry_content = request.form.get("content")
            formated_date = datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formated_date})
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]

        return render_template("home.html", entries=entries_with_date)

    return app






