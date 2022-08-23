import os.path

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask import request
from db.api import insert_product, get_products

app = Flask(__name__)
CORS(app)

API_URL = "/api/v1/"
app.config["UPLOAD_FOLDER"] = "/upload/"

@app.route(f"{API_URL}upload/<image>")
def get_image(image):
    return send_from_directory("../upload/", image, as_attachment=True)

@app.route(API_URL + "get-products")
def get_products_controller():
    return get_products()

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
    status = "Success"
    try:
        insert_product(product)
    except:
        status = "Error"
    return {"Staus": status}


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="localhost", port=3001)
