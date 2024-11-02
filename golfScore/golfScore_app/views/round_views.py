from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.views.generic import ListView
from golfScore_app.models import GolfHouseMaster

# # Create your views here.
# def helloworld(request):
#     return HttpResponse('round Hello World!')
def test(request):
    return HttpResponse('round test')

class helloworld(ListView):
    model = GolfHouseMaster
    template_name = 'round_pages/list_golfhouse.html'
    
