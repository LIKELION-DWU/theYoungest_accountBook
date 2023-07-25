from django.shortcuts import render
from .models import AccountBook, Type1, Type2, Type3
from .serializers import BookSerializer, Type1_Serializer, Type2_Serializer, Type3_Serializer
from rest_framework.viewsets import ModelViewSet

class BookViewSet(ModelViewSet) :
    queryset = AccountBook.objects.all()
    serializer_class = BookSerializer
    
    # def get_queryset(self, request):
    #     type_name = request['type_name'] # type_name을 받아옴 -> type을 고르면 
    #     if type_name == None :
    #         type_name = "Type1"
    #     return self.queryset.filter(type_name=type_name)
    

class Type1_ViewSet(ModelViewSet) :
    queryset = Type1.objects.all()
    serializer_class = Type1_Serializer
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['book_id']
        return self.queryset.filter(accountBook=id)

class Type2_ViewSet(ModelViewSet) :
    queryset = Type2.objects.all()
    serializer_class = Type2_Serializer
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['book_id']
        return self.queryset.filter(accountBook=id)

class Type3_ViewSet(ModelViewSet) :
    queryset = Type3.objects.all()
    serializer_class = Type3_Serializer
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['book_id']
        return self.queryset.filter(accountBook=id)