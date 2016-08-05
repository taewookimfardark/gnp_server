from . import api
from application import db
from application.models.record import(, UserPlayerRecord,MatchRecord)

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

#@api.route('/recordusers',methods=['POST'])
#def post_record_users():



