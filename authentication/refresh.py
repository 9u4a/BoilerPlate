from datetime import datetime, timedelta

import jwt


def RefreshToken(obj):
    userObj = obj
    token = jwt.encode(
        {'user_id': userObj.user_id,
         'exp': datetime.utcnow() + timedelta(days=14)},
        'boiler', algorithm='HS256'
    )

