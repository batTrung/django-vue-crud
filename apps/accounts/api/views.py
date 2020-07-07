from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response


class CheckEmailExists(APIView):
    name = 'check-email-exists'

    def get(self, request, email, format=None):
        email_exists = get_user_model().objects.filter(email=email).exists()
        return Response({
            'invalid': email_exists,
        })
