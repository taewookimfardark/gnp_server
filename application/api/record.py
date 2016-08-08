from . import api
from application import db
from application.models.user import User
from application.models.match import Match
from application.models.record import(PlayerRecord, MatchRecord)

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

@api.route('/recordusers',methods=['POST'])
def post_record_users():
    request_params = request.get_json()
    for param in request_params:
        userid = param.get('userid')
        matchid = param.get('matchid')
        point = param.get('point')
        assist = param.get('assist')
        rebound = param.get('rebound')
        temp_record = MatchRecord(userid=userid,matchid=matchid,point=point,assist=assist,rebound=rebound)
        db.session.add(temp_record)
    db.session.commit()

    return "success"

@api.route('/recordmatches/<int:matchid>', methods=['PUT'])
def put_match_user_record(matchid):
    match = Match.query.get(matchid)
    matchparam = request.get_json()[0]
    match.finish = matchparam.get('finish')
    match.win = matchparam.get('win')
    match.matchinfo = matchparam.get('matchinfo')
    match.score_gnp = matchparam.get('scoregnp')
    match.score_enemy = matchparam.get('scoreenemy')
    db.session.commit()

    userparam = request.get_json()[1]
    for param in userparam:
        print(param.get('point'))
        print(type(param.get('point')))
        temp_user = db.session.query(PlayerRecord).filter(PlayerRecord.userid==param.get('userid')).one()
        print(temp_user.points)
        print(type(temp_user.points))
        print(temp_user.points + param.get('point'))
        print(type(temp_user.points + param.get('point')))
        temp_user.games = temp_user.games+1
        temp_user.points = temp_user.points + param.get('point')
        temp_user.assists = temp_user.assists + param.get('assist')
        temp_user.rebounds = temp_user.rebounds + param.get('rebound')
    db.session.commit()

    return "success"







