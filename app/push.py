"""
POST    /pushinfo
"""

import sys
import random
from app import *
from app.model import *
from flask import jsonify, request, session

@application.route('/pushinfo', methods=['GET'])
def pushnoti():
    _from = ['LongChen',
     'ZihanTong',
     'ZhenLi',
     'JiaHengZhang']
    _to = ['Mandy',
     'MeiMeiHan',
     'Hana',
     'Wendy']
    _activity = ['Apply', 'Approved', 'Accept']
    _target = ['Shopping to Ralphs', 'Go to cinema', 'Go to Gun club']
    string = random.choice(_from)
    return jsonify(results={'from': random.choice(_from),
     'to': random.choice(_to),
     'action': random.choice(_activity),
     'events': random.choice(_target)})
#+++ okay decompyling push.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.01.31 10:08:02 PST
