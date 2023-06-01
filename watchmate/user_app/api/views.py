from rest_framework.views import APIView
from user_app.api.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status


class register_view(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Regestration successful!!"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
    
class logout_view(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    