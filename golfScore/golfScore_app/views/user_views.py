from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
#from golfScore_app.forms import SignUpForm # forms.py未完成

# Create your views here.
def helloworld(request):
    return HttpResponse('user Hello World!')
def test(request):
    return HttpResponse('user test')

# アカウント登録処理
class UserSignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_pages/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # ここで追加の処理を行うことができます
        return response

    

# ログイン処理
class UserLoginView(LoginView):
    template_name = 'user_pages/login_signup.html'
    def form_valid(self, form):        
        return super().form_valid(form)
    
# ログアウト処理
class UserLogoutView(LogoutView):
    next_page = '/login/'
