from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer,EmailSerializer
import logging

logger = logging.getLogger(__name__)

class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class MicrosoftAuthView(APIView):
    logger.info('0110')
    def post(self, request):
        logger.info('011')
        access_token = request.data.get('access_token')
        logger.info('012')
        if not access_token:
            logger.info('013')
            return Response({"error": "Access token is required"}, status=status.HTTP_400_BAD_REQUEST)
        logger.info(access_token)
        logger.info('014')

        # Verify the token with Microsoft Graph API
        graph_url = 'https://graph.microsoft.com/v1.0/me'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(graph_url, headers=headers)
        print(response.status_code)

        if response.status_code != 200:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        user_info = response.json()
        email = user_info.get('mail') or user_info.get('userPrincipalName')

        # Find or create a user in your database
        user, created = User.objects.get_or_create(username=email, defaults={"email": email})
        if created:
            # Set a default password
            default_password = "1q2w3e4r"
            user.set_password(default_password)
            user.save()

        # Generate JWT token for the user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    
class GoogleAuthView(APIView):
    def post(self, request):
        email = request.data.get('email')
        serializer = EmailSerializer(data={'email':email})
        if not serializer.is_valid():
            return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)
        user, created = User.objects.get_or_create(username=email)
        if created:
            # Set a default password
            default_password = "1q2w3e4r"
            user.set_password(default_password)
            user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })        
            


