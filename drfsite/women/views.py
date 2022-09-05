from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Women, Category
from .serializers import WomenSerializer

class WomenViewSet(viewsets.ModelViewSet):
    #queryset = Women.objects.all() - Выбор всех полей, для работы нужно добавить basename в urls
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk) # get_queryset должен возвращать список, поэтому берем запись через фильтр

    @action(methods=['get'], detail=True) # detail=False выключает поиск по id
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': [cats.name]})

"""
Пример через базовый класс APIView
class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'put': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        
        # Код для удаления записи

        return Response({'delete': 'delete post ' + str(pk)})
"""

"""
Пример через специальные классы APIView
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
"""