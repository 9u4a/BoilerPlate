from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from authentication.access import AccessToken
from authentication.refresh import RefreshToken

from ..models import User


class LoginView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user = User.objects.get(user_id=data['user_id'])
        print(user)
        if not user:
            response = {
                'success': False,
                'err': '존재하지 않는 id입니다.'
            }
            return JsonResponse(response, status=400)
        if data['user_pw'] != user.user_pw:
            response = {
                'success': False,
                'err': '비밀번호가 일치하지 않습니다.'
            }
            return JsonResponse(response, status=400)
        refresh_token = RefreshToken(user)
        access_token = AccessToken(user)
        response = JsonResponse({
            'success': True,
            'jwt_token': {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        }, status=200)
        response.set_cookie('access_token', access_token, httponly=True)
        response.set_cookie('refresh_token', refresh_token, httponly=True)
        return response
