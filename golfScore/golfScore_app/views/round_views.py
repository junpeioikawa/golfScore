from django.http.response import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('round Hello World!')
def test(request):
    return HttpResponse('round test')
