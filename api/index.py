from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/get-products")
def getProducts():
    return {"hello": "from python!"}

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=3001)
