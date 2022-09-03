import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Women

"""Пример как устроена работа сериализатора вместе с моделью"""
class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()

def encode():
    model = WomenModel('Angelina Jolie', 'Women actor')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"Angelina", "content":"Angelina`s content"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer): - Работа напрямую с моделью
#     class Meta:
#     model = Women
#     fields = ('title', 'cat_id')