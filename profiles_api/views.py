from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    # Test API View
    def get(self, request, format=None):
        # Returns a list of API features
        an_apiview = [
            'Uses HTTP methods(get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you most control over application',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
