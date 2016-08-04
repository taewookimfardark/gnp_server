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

@api.route('/matches', methods=['POST'])
def post_matches():
    request_params = request.get_json()
    tag = request_params.get('tag')
    against = request_params.get('against')
    where = request_params.get('where')
    when = request_params.get('when')
    matchinfo = request_params.get('matchinfo')
    score_gnp = request_params.get('score_gnp')
    score_enemy = request_params.get('score_enemy')
    finish = request_params.get('finish')
    win = request_params.get('win')

    match = Match(tag=tag,against=against,where=where,when=when,matchinfo=matchinfo,score_gnp=score_gnp,score_enemy=score_enemy,finish=finish,win=win)
    db.session.add(match)
    db.session.commit()
    return jsonify(
        data=model_to_dict(match),
    )