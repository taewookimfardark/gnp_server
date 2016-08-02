from functools import wraps
from application.models.user import User
from flask import request, jsonify
from application.lib.jwt.jwt_helper import jwt_decode


def required_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        error_response = jsonify(
            userMessage="Authorization required"
        ), 401

        try:
            token_string = request.headers.get('Authorization')
        except:
            return error_response

        print token_string

        try:
            decoded_user = jwt_decode(token_string)
            decoded_user_id = decoded_user['id']
        except:
            return error_response #TODO invalide token data

        if User.query.filter(
                        User.id == decoded_user_id).count() == 0:
            return error_response #TODO not found user

        return f(*args, **kwargs)

    return decorated_function


def get_user_data_from_request(request):
    """

    :param request:
    :return: user data dic { "id": , "email", }
    """
    token_string = request.headers.get('Authorization')
    return jwt_decode(token_string)
