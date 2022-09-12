import os
from traceback import print_tb
import jwt
from flask import Flask, send_from_directory, send_file, request, Response
from flask_cors import CORS, cross_origin
from db.api import *
from dotenv import load_dotenv


import bcrypt

load_dotenv()

app = Flask(__name__)
CORS(app, resources="*")

API_URL = "/api/v1/"
app.config["UPLOAD_FOLDER"] = "/upload/"

def check_token(req):
    token = req.headers["Authorization"].split(" ")[1]
    decoded = jwt.decode(jwt=token, key=os.getenv("JWT_SECRET"), algorithms="HS256")

    try:
        user = find_user(decoded["login"])
        return True, bcrypt.checkpw(
            password=bytes(decoded["password"], "utf-8"), 
            hashed_password=bytes(user["password"], "utf-8")
        )
    except:
        print("Authorize error")
        return False, Response("{'Status':'Unauthorized user'}", status=401, mimetype="application/json")
   
@app.route("/")
def root():
    return send_from_directory("static", "index.html")

@app.route("/static/<path>")
def send_static(path):
    print("adawd;.a[d.lwa[dla[dla[pwdlw[")
    return ""

# Users
@app.post(API_URL + "login-user")
def login_user_controller():
    body = request.form.to_dict()
    password = bytes(body["password"], "utf-8")
    finded_user = find_user(body["login"])
    status = False
    
    is_password_correct = bcrypt.checkpw(
        password=password, 
        hashed_password=bytes(finded_user["password"], "utf-8")
    )
    token = "Login or password is incorect"

    if is_password_correct:
        status = True
        token = jwt.encode(payload=body, key=os.getenv("JWT_SECRET"), algorithm="HS256")

    
    return {"status": status, "token": token}
    

# Products
@app.route(f"{API_URL}upload/<image>")
def get_image(image):
    return send_from_directory("upload/", image, as_attachment=True)

@app.route(API_URL + "get-products")
def get_products_controller():
    print("bebra")
    return get_products()

@app.route(API_URL + "get-product")
def get_product_controller():
    id = request.args.get("id")
    
    return get_product(id)
    
@app.post(API_URL + "create-product")
def create_product_controller():
    check = check_token(req=request)

    if check[0]:
        body = request.form.to_dict()
        image = request.files["image"]
        image.save(os.path.join(os.path.join("upload"), image.filename))

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
        return {"status": status}
    else:
        return check[1]

@app.delete(API_URL + "delete-product")
def delete_product_controller():
    check = check_token(req=request)
    if check[0]:
        id = request.args.get("id")
        status = "Success"
        try:
            delete_product(id)
        except:
            status = "Error"
        return {"status": status}
    else:
        return check[1]


@app.patch(API_URL + "edit-product")
def edit_product_controller():
    check = check_token(req=request)
    if check[0]:
        body = request.form.to_dict()
        product = {
            "name": body["name"],
            "description": body["description"],
        }

        if len(request.files):
            image = request.files["image"]
            image.save(os.path.join(os.path.join("upload"), image.filename))
            product["image"] = f"/upload/{image.filename}"

        status = "Success"

        try:
            edit_product(product, request.args.get("id"))
        except:
            status = "Error"
        return {"status": status}
    else:
        return check[1]


if __name__ == "__main__":
    print('serve is started')
    app.run('0.0.0.0', port=5000)
    
