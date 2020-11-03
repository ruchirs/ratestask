from rest_framework.response import Response
import datetime
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, generics
from rest_framework import status
from .models import  Prices
from .serializer import PriceSerializer
from rest_framework.decorators import api_view

class PriceList(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = PriceSerializer
    def post(self, request, format=None):
        serializers = PriceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def query_set(request):
    if request.method == "GET":
        # print(request.query_params)
        start = request.query_params.get('date_from', None)
        year1, month1, day1 = start.split('-')
        end = request.query_params.get('date_to', None)
        year2, month2, day2 = end.split('-')
        date1 = datetime.date(int(year1), int(month1), int(day1))
        date2= datetime.date(int(year2), int(month2), int(day2))
        result = Prices.objects.filter(date__gte=date1, date__lte=date2)

        def daterange(date1, date2):
            for n in range(int((date1 - date2).days)):
                yield start_date + timedelta(n)
        for d in daterange(date1, date2):
            lst=[]
            for i in result:
                if i.date == d:
                    lst.append(i.price)
                    # do the less than three handling
                    if len(lst) > 3:
                        average = sum(lst)/len(lst)
                    else:
                        average = None
            return Response({d:average})

    return Response('bad request', status=status.HTTP_400_BAD_REQUEST)