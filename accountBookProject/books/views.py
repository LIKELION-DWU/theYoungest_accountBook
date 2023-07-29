from django.shortcuts import render
from .models import AccountBook, Type1, Type2, Type3
from .serializers import BookSerializer, Type1_Serializer, Type2_Serializer, Type3_Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum

class BookViewSet(ModelViewSet):
    queryset = AccountBook.objects.all()
    serializer_class = BookSerializer

class TypeViewSet(ModelViewSet):

    def get_object(self):
        # 오버라이드하여 해당 book_id의 AccountBook을 반환
        book_id = self.kwargs.get('book_id')
        return get_object_or_404(AccountBook, id=book_id)

    def get_queryset(self):
        account_book = self.get_object()
        self.calculate_total() 

        type_name = account_book.type_name
        if type_name == 'Type1':
            return account_book.type1_set.all()
        elif type_name == 'Type2':
            return account_book.type2_set.all()
        elif type_name == 'Type3':
            return account_book.type3_set.all()
        else:
            return Type1.objects.none() 
        
    def calculate_total(self):
        account_book = self.get_object()
        if account_book.type_name == 'Type1':
            total_money = account_book.type1_set.aggregate(total=Sum('money'))['total']
        elif account_book.type_name == 'Type2':
            total_money = account_book.type2_set.aggregate(total=Sum('money'))['total']
        elif account_book.type_name == 'Type3':
            total_money = account_book.type3_set.aggregate(total=Sum('money'))['total']
        else:
            total_money = 0

        account_book.total = total_money if total_money is not None else 0
        account_book.save()

    def get_serializer_class(self):
        account_book = self.get_object()
        type_name = account_book.type_name
        if type_name == 'Type1':
            return Type1_Serializer
        elif type_name == 'Type2':
            return Type2_Serializer
        elif type_name == 'Type3':
            return Type3_Serializer
        else:
            return Type1_Serializer 
