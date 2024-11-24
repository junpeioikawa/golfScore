from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from golfScore_app.forms import SignupForm # forms.py未完成

# Create your views here.
def helloworld(request):
    return HttpResponse('user Hello World!')
def test(request):
    return HttpResponse('user test')

# アカウント登録処理
class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'user_pages/signup.html'
    
    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)    
        return valid
    

# ログイン処理
class UserLoginView(LoginView):
    template_name = 'user_pages/login.html'
    def form_valid(self, form):        
        return super().form_valid(form)
    
# ログアウト処理
class UserLogoutView(LogoutView):
    next_page = '/login/'
