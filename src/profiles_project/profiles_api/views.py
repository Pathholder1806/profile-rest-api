from django.shortcuts import render

from rest_framework import viewsets #This is the base module for all the viewsets that django REST framework offers.

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):    #This is same as GET function as in APIView.
        """Retruns a hello message."""

        a_viewset =[
            'Uses actions(list, create, retrieve, update, partial update, partial update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.',
        ]

        return Response({'message': 'Hello!', 'a_viewset' : a_viewset})


    def create(self, request):
        """Creates a hello message with our name."""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'Message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handles getting an object bt it's ID."""

        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method' : 'PATCH'})


    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method' : 'DELETE'})
