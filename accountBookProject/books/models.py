from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User

# main account book
class AccountBook(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(verbose_name="날짜")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type_name = models.TextField(verbose_name="type명", default="Type1")
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)


class Type1(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE, related_name='type1_set')
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.money)


class Type2(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE, related_name='type2_set')
    category = models.TextField()
    memo = models.TextField()
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.money)


class Type3(models.Model):
    accountBook = models.ForeignKey(AccountBook, on_delete=models.CASCADE, related_name='type3_set')
    content = models.TextField()
    image = models.ImageField(verbose_name='이미지', blank=True, null=True, upload_to='post-image')
    money = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.money)
