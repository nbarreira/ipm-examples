from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from time import sleep
from random import randint
import io
import os
import sys


from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
CORS(app)


# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

    else:
        username = request.form['username']
        password = request.form['password']

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    sleep(randint(2,4))
    return jsonify(logged_in_as=current_user), 200


@app.route('/image', methods=['GET'])
def image():
    images = ['logo_udc.png', 'logo_fic.png', 'logo_coruna.png']
    imagename = images[randint(0,2)]
    print(imagename)
    file = open(os.getcwd() + '/'+ imagename, 'rb')
    return send_file(io.BytesIO(file.read()),
        mimetype='image/png',
        as_attachment=True,
        attachment_filename=imagename)

if __name__ == '__main__':
    app.run()
