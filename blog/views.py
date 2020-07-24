from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from .models import Blog
from django.shortcuts import  redirect
from django.views.generic import CreateView, ListView
from .forms import RegisterForm, BlogPost




# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'index.html'


class Blog(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'obj'
    login_url = 'blogs:login'

    def handle_no_permission(self):
         # pass None to redirect_field_name in order to remove the next param
         return redirect_to_login(self.request.get_full_path(), self.get_login_url(), None)


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


class PostCreate(LoginRequiredMixin,CreateView):

    form_class = BlogPost
    model = Blog
    template_name = 'blog/Createpost.html'
    success_url = reverse_lazy('blog:blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





