from django.shortcuts import render

from rest_framework.views import APIView    #This imports the APIView class from the django REST Framework.
from rest_framework.response import Response   #Standard response object that we return from our APIView and that can be rendered into an API output.
from rest_framework import status    #It contains HTTP standard codes like HTTP 404,etc.

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, put, post, patch delete)',
            'It is similar to traditional django view',
            'Gives you most control over your logic',
            'Is mapped manually to URLs.'
        ]

        return Response({'message' : "Hello!", 'an_apiview' : an_apiview})


    def post(self, request):
        """Creates a hello message with our name."""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'Message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates the fields provided in the request."""

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method' : 'delete'})
