from rest_framework.serializers import ModelSerializer
from .models import AccountBook, Type1, Type2, Type3

class BookSerializer(ModelSerializer) :
    class Meta: 
        model = AccountBook
        fields = ['id', 'title', 'date', 'type_name', 'total']

class Type1_Serializer(ModelSerializer) :
    class Meta:
        model = Type1
        fields = ['id','accountBook', 'money']

class Type2_Serializer(ModelSerializer) :
    class Meta:
        model = Type2
        fields = ['id','accountBook', 'category', 'memo', 'money']

class Type3_Serializer(ModelSerializer) :
    class Meta:
        model = Type3
        fields = ['id','accountBook', 'money', 'content', 'image']