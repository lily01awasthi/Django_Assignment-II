
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView,ListView
from .forms import RegisterForm


from django.contrib import messages


# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'index.html'


class Blog(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'obj'



class Register(CreateView):
    form_class = RegisterForm
    form = form_class
    template_name = 'blog/register.html'
    model = User
    success_url = 'blogs:login'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return redirect(self.success_url)



