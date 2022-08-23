import os.path

from flask import Flask
from flask_cors import CORS
from flask import request
from db.api import insert_product

def get_server_app():
    app = Flask(__name__)
    CORS(app)

    API_URL = "/api/v1/"
    app.config["UPLOAD_FOLDER"] = "/upload/"
    return app

@app.route(API_URL + "get-products")
def get_products_controller():
    return {"Hello": "123"}

@app.post(API_URL + "create-product")
def create_product_controller():
    body = request.form.to_dict()
    image = request.files["image"]
    image.save(os.path.join(os.path.join("../upload"), image.filename))

    product = {
        "name": body["name"],
        "description": body["description"],
        "image": f"/upload/{image.filename}"
    }

    insert_product(product)
    return {"DAD": "DADA"}


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=3001)
