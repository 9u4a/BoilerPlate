from datetime import datetime, timedelta
import jwt


def AccessToken(obj):
    token = jwt.encode(
        {'user_id': obj.user_id,
         'exp': datetime.utcnow() + timedelta(minutes=30)},
        'boiler', algorithm='HS256'
    )
    return token
