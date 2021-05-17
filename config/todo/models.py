from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
class Todo(models.Model):
    author=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    name=models.CharField(("نام شما"), max_length=300)
    title=models.CharField(("عنوان"), max_length=300)
    description=models.TextField(("توضیحات"))
    email=models.EmailField(("ایمیل"), max_length=254)
    start_date = models.DateTimeField(("زمان شروع"), default=timezone.now)
    end_date=  models.DateTimeField(("زمان پایان"),default=timezone.now)
    

    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")

    def __str__(self):
        return self.name

