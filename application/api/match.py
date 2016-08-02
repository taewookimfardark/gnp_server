from . import api
from application import db
from application.models.match import Match

from flask import request, jsonify
from application.lib.rest.rest_query_helper import (
    model_to_dict
)
from application.lib.rest.auth_helper import (
    get_user_data_from_request,
    required_token
)

#from application.lib.storage.cloud_storage_helper import upload_image

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@api.route("/matches", methods=['GET'])
def get_matches():
    matches = Match.query.all()
    query_list = []
    for match in matches:
        temp = model_to_dict(match)
        query_list.append(temp)
    print(query_list)

    return jsonify(
        data = query_list
    )
