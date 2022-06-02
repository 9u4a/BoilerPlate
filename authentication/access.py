from datetime import datetime, timedelta

import jwt


def AccessToken(obj):
    userObj = obj
    token = jwt.encode(
        {'user_id': userObj.user_id,
         'exp': datetime.utcnow() + timedelta(minutes=30)},
        'boiler', algorithm='HS256'
    )

