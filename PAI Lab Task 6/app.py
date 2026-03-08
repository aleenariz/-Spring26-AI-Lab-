from flask import Flask, render_template, request
from detect import detect_animals
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            count, output_path = detect_animals(filepath)

            return render_template("index.html",
                                   count=count,
                                   image=output_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)