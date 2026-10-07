from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Website Flask</title>
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <header>
    Website Flask
  </header>
</body>
<html>"""

@app.route("/css/style.css")
def css():
  return Response("""* {
  box-sizing: border-box;
}
html {
  scroll-behavior: smooth;
}
body {
  margin: 0;
  font-family: system-ui, Arial, sans-serif;
  background: #f4f4f4;
}
header {
  background: #3498db;
  padding: 20px;
  text-align: center;
  color: #fff;
  font-weight: bold;
  font-size: clamp(3rem, 8vw, 6rem);
  margin-bottom: 30px;
}
.container {
  margin: 10px;
}""",
                  content_type = "text/css"
                 )
if "__main__" == __name__:
    app.run(host="0.0.0.0", port=8080)
