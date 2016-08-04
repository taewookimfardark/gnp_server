from . import api
from application import db
from application.models.user import User

from flask import request, jsonify
from application.lib.rest.rest_query_helper import (
    model_to_dict
)
from application.lib.rest.auth_helper import (
    get_user_data_from_request,
    required_token
)

from sqlalchemy import and_
from sqlalchemy import or_

#from application.lib.storage.cloud_storage_helper import upload_image

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@api.route("/")
def heool():
    return "hello woohwa"

@api.route("/users", methods=['GET'])
def get_users():
    users = User.query.all()
    query_list = []
    for user in users:
        temp = model_to_dict(user)
        query_list.append(temp)
    print(query_list)

    return jsonify(
        data = query_list
    )

@api.route('/users', methods=['POST'])
def post_users():
    request_params = request.get_json()
    email = request_params.get('email')
    password = request_params.get('password')
    backnumber = request_params.get('backnumber')
    name = request_params.get('name')
    info = request_params.get('info')
    q = db.session.query(User).filter(User.email == email)
    if q.count() > 0:
        return jsonify(
            userMessage="your email is already enrolled"
        )
    user = User(email=email, password=password, name=name,info=info, backnumber=backnumber)
    db.session.add(user)
    db.session.commit()
    return jsonify(
        data=model_to_dict(user),
        token=user.get_token_string()
    )

@api.route('/login', methods=['POST'])
def login():
    request_params = request.get_json()
    email = request_params.get('email')
    password = request_params.get('password')
    user = db.session.query(User).filter(and_(User.email == email, User.password == password)).first()
    if user is None:
        return jsonify(
            userMessage="Please check your email or password"
        )
    data = model_to_dict(user)
    return jsonify(
        data=data
    )


