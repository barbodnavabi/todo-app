from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
class Todo(models.Model):
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

    # def get_absolute_url(self):
    #     return reverse("todo_detail", kwargs={"pk": self.pk})
