from django.shortcuts import redirect

from blog.views import Blog


class MyCustomMiddleWare:
    def __init(self,get_response):
        self.get_response = get_response

    def __ceil__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user:
            if not request.user.is_authenticated and view_func == Blog:
                return redirect('login')
