from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from rest_framework import status
from .models import  Prices
from .serializer import PriceSerializer

#........
class PriceList(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    # queryset = Prices.objects.all()
    serializer_class = PriceSerializer

    def post(self, request, format=None):
        serializers = PriceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)