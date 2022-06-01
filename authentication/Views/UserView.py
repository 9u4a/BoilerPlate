from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from authentication.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            response = {'success': True}
        else:
            response = {'success': False}
        return JsonResponse(response)



