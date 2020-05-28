from django.shortcuts import render

from rest_framework.views import APIView    #This imports the APIView class from the django REST Framework.
from rest_framework.response import Response   #Standard response object that we return from our APIView and that can be rendered into an API output.

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, put, post, patch delete)',
            'It is similar to traditional django view',
            'Gives you most control over your logic',
            'Is mapped manually to URLs.'
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
