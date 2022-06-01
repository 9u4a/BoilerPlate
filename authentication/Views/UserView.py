from django.http import HttpResponse
from rest_framework.views import APIView


class UserView(APIView):
    def post(self, request):
        return HttpResponse(status=404)
