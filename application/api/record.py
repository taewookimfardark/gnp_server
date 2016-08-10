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

@api.route('/recordplayers', methods=['GET'])
def get_record_players():
    player_records = PlayerRecord.query.all()
    query_list = []
    for record in player_records:
        temp = model_to_dict(record)
        print temp
        query_list.append(temp)
    return jsonify(
        data = query_list
    )

@api.route('/recordmatches', methods=['GET'])
def get_record_matches():
    match_records = MatchRecord.query.all()
    query_list = []
    for record in match_records:
        temp = model_to_dict(record)
        query_list.append(temp)
    return jsonify(
        data = query_list
    )


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
    print request.get_json()
    match = Match.query.get(matchid)
    matchparam = request.get_json()[0]
    match.finish = matchparam.get('finish')
    match.win = matchparam.get('win')
    match.matchinfo = matchparam.get('matchinfo')
    match.score_gnp = matchparam.get('scoregnp')
    match.score_enemy = matchparam.get('scoreenemy')
    db.session.add(match)
    db.session.commit()

    userparam = request.get_json()[1]
    for param in userparam:
        print param
        if(param.get('ischecked')==True):
            # print param
            # print param.get('userid')
            # print type(param.get('userid'))
            print "loop"
            temp_user = db.session.query(PlayerRecord).filter(PlayerRecord.userid==int(param.get('userid'))).first()
            print temp_user
            temp_user.games = int(temp_user.games)+1
            temp_user.points = int(temp_user.points) + param.get('point')
            temp_user.assists = int(temp_user.assists) + param.get('assist')
            temp_user.rebounds = int(temp_user.rebounds) + param.get('rebound')
            db.session.add(temp_user)
    db.session.commit()

    return "success"

@api.route('/playerrecord/page', methods=['GET'])
def player_record_page():
    playerrecords = PlayerRecord.query.all()
    data = []
    for playerrecord in playerrecords:
        temp = []
        temp_user_data = User.query.get(playerrecord.userid)
        temp.append(model_to_dict(temp_user_data))
        temp.append(model_to_dict(playerrecord))
        data.append(temp)
    return jsonify(
        data=data
    )







