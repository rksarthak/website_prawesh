from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    lang = request.args.get("lang", "en")
    if lang == "nl":
        return render_template("index_nl.html")
    return render_template("index_en.html")

@app.route("/submitted", methods=["POST"])
def submitted():
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")
    return render_template("submitted.html", name=name, phone=phone, message=message)



if __name__ == "__main__":
    app.run(debug=True)

