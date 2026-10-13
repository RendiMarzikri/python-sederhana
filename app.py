from flask import Flask, render_template, Response
app = Flask(__name__, template_folder="template")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/css/style.css")
def css():
    return Response("body{font-family:Arial;background:#111;color:white;text-align:center;padding:50px}button{padding:10px}", content_type="text/css")
@app.route("/api")
def api():
    return {"status": "success", "message": "Flask berjalan!"}
