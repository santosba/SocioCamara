from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from account import models

# Create your views here.

class LogoutView(APIView):
    
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)
        
        

@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data = request.data)
        data = {}
        if serializer.is_valid():           
            account = serializer.save()
            data['response'] = 'Successful Registration !'
            data['username'] = account.username
            data['email']  = account.email
            data['first_name'] = account.first_name
            # when using token authentication, you can uncomment the following lines
            token = Token.objects.get(user=account).key
           # refresh = RefreshToken.for_user(account)

            '''
            data['token'] = {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }
            
            '''
        
            data['token'] = token
            
            return Response(data ,status= status.HTTP_201_CREATED) 
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)



        
