import jwt
from django.http import HttpResponse, JsonResponse
from jwt import ExpiredSignatureError

from authentication.access import AccessToken
from models import User


# encoded_jwt = jwt.encode({"user_pw": "jun1234"}, "boiler", algorithm="HS256")

def DecodeToken(request):
    token = request.COOKIE.get('jwt')
    try:
        token = jwt.decode(token, 'boiler', algorithms=["HS256"])
        userObj = User.objects.get(user_pw=token['user_pw'])
        if userObj.user_id == token['user_id']:
            return userObj
    except ExpiredSignatureError:
        return JsonResponse({"success": False, "err": "토큰 만료"}, status=400)
    AccessToken(userObj)
