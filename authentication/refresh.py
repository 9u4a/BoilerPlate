from datetime import datetime, timedelta

import jwt


def RefreshToken(obj):
    token = jwt.encode(
        {'user_id': obj.user_id,
         'exp': datetime.utcnow() + timedelta(days=14)},
        'boiler', algorithm='HS256'
    )
    return token

