from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        return JsonResponse()
