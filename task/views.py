from rest_framework.response import Response
import datetime
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework import status
from .models import  Prices
from .serializer import PriceSerializer
from rest_framework.decorators import api_view

#........
class PriceList(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    # queryset = Prices.objects.all()
    serializer_class = PriceSerializer
    # serializer_class = PriceSerializer
    # def get_queryset(self):

    #     param = self.kwargs.get('pk')
    #     param2 = self.kwargs.get('sk')
    #     param3 = self.kwargs.get('ek')
    #     return Prices.objects.filter(origin_code=param, date__gte = param2, date__lte = param3)

    def post(self, request, format=None):
        serializers = PriceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def query_set(request):
    if request.method == "GET":
        print(request.query_params)
        start = request.query_params.get('date_from', None)
        year1, month1, day1 = start.split('-')
        end = request.query_params.get('date_to', None)
        year2, month2, day2 = end.split('-')
        result = Prices.objects.filter(date__gte=datetime.date(int(year1), int(month1), int(day1)),
                                date__lte=datetime.date(int(year2), int(month2), int(day2)))
        print(result)
        serializer = PriceSerializer(result, many=True)
        p=serializer.data
        print(p)
        return Response(p, status=status.HTTP_200_OK)
    return Response('bad request', status=status.HTTP_400_BAD_REQUEST)