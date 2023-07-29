from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import AccountBook, Type1, Type2, Type3
from .serializers import BookSerializer, Type1_Serializer, Type2_Serializer, Type3_Serializer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum

class BookViewSet(ModelViewSet):
    queryset = AccountBook.objects.all()
    serializer_class = BookSerializer

class TypeViewSet(ModelViewSet):
    def get_account_book(self):
        book_id = self.kwargs.get('book_id')
        account_book = get_object_or_404(AccountBook, id=book_id)
        return account_book

    def get_object(self):
        type_id = self.kwargs.get('pk')
        account_book = self.get_account_book()

        type_model = None
        if account_book.type_name == 'Type1':
            type_model = get_object_or_404(Type1, id=type_id, accountBook=account_book)
        elif account_book.type_name == 'Type2':
            type_model = get_object_or_404(Type2, id=type_id, accountBook=account_book)
        elif account_book.type_name == 'Type3':
            type_model = get_object_or_404(Type3, id=type_id, accountBook=account_book)

        return type_model

    def calculate_total(self):
        account_book = self.get_account_book()
        if account_book.type_name == 'Type1':
            total_money = account_book.type1_set.aggregate(total=Sum('money'))['total']
        elif account_book.type_name == 'Type2':
            total_money = account_book.type2_set.aggregate(total=Sum('money'))['total']
        elif account_book.type_name == 'Type3':
            total_money = account_book.type3_set.aggregate(total=Sum('money'))['total']

        account_book.total = total_money if total_money is not None else 0
        account_book.save()

    def get_serializer_class(self):
        account_book = self.get_account_book()
        type_name = account_book.type_name
        if type_name == 'Type1':
            return Type1_Serializer
        elif type_name == 'Type2':
            return Type2_Serializer
        elif type_name == 'Type3':
            return Type3_Serializer
        else:
            return Type1_Serializer 

    def get_queryset(self):
        account_book = self.get_account_book()
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.calculate_total()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        self.calculate_total()
        return Response(status=status.HTTP_204_NO_CONTENT)