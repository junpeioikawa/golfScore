from django.db.models.query import QuerySet
from django.utils import dateformat,timezone
from django.utils.timezone import localtime

from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
from django.views.generic import ListView
from golfScore_app.models import GolfHouseMaster

# # Create your views here.
# def helloworld(request):
#     return HttpResponse('round Hello World!')
# def test(request):
#     return HttpResponse('round test')

def list_golfHouse_View(request):
    golfHouseList = GolfHouseMaster.objects.all()
    dispData = {
        'title':'タイトル',
        'golfHouseList':golfHouseList,
    }
    return render(request, 'round_pages/list_golfhouse.html', dispData)

def input_round_View(request):
    print(request.GET["id"])


class GolfHouseListView(ListView):
    model = GolfHouseMaster
    # model['title'] = 'GolfHouseListViewのタイトル'
    template_name = 'round_pages/list_golfhouse.html'
    def get_context_data(self):
            dispData = super().get_context_data()
            # page_title を追加する
            dispData['title'] = 'hoge'
            d = timezone.now()
            dt_now = d.strftime('%Y/%m/%d %A %H:%M:%S')

            dispData['date'] = dt_now
            
            return dispData
