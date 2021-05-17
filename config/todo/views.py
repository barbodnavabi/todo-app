from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = "todo/index.html"
    fields=['name','title','email','description','start_date','end_date']
    success_url= reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] =  Todo.objects.all()
        return context
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        form.save()
        return super().form_valid(form)

# def index(request):
#     todo_list=Todo.objects.all()
#     conext ={
#         'todo_list':todo_list

#     }
#     return render(request,'todo/index.html',conext)