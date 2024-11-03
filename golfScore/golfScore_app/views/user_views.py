from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
#from golfScore_app.forms import SignUpForm # forms.py未完成

# Create your views here.
def helloworld(request):
    return HttpResponse('user Hello World!')
def test(request):
    return HttpResponse('user test')

# アカウント登録処理
class SignUpView(CreateView):
    # form_class = SignUpForm
    success_url = '/login/'
    template_name = 'user_pages/login_signup.html'
    
    def form_valid(self, form):    
        return super().form_valid(form)
    

# ログイン処理
class UserLoginView(LoginView):
    template_name = 'user_pages/login_signup.html'
    def form_valid(self, form):        
        return super().form_valid(form)
    
