from django.db import models
from django.contrib.auth.models import User

# main account book
class AccountBook(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(verbose_name="날짜")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type_name = models.TextField(verbose_name="type명", default="Type1")
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# type1
class Type1(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.money

#type2
class Type2(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE)
    category = models.TextField()
    memo = models.TextField()
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.money

#type3
class Type3(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post-image')
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.money