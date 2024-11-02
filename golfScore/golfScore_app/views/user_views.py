from django.http.response import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('user Hello World!')
def test(request):
    return HttpResponse('user test')