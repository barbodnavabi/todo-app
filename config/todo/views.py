from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import CreateView
class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/index.html"
    fields=['name','title','email','description','start_date','end_date']
    success_url= reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] =  Todo.objects.all()
        return context
    


# def index(request):
#     todo_list=Todo.objects.all()
#     conext ={
#         'todo_list':todo_list

#     }
#     return render(request,'todo/index.html',conext)