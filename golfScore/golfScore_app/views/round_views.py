from django.db.models.query import QuerySet
from django.utils import dateformat,timezone
from django.utils.timezone import localtime

from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
from django.views.generic import ListView,CreateView
from golfScore_app.models import GolfHouseMaster,Round

# # Create your views here.
# def helloworld(request):
#     return HttpResponse('round Hello World!')
# def test(request):
#     return HttpResponse('round test')

class GolfHouseListView(ListView):
    model = GolfHouseMaster
    template_name = 'round_pages/list_golfhouse.html'
    def get_context_data(self):
            disp_data = super().get_context_data()
            # page_title を追加する
            disp_data['title'] = 'hoge'
            d = timezone.now()
            dt_now = d.strftime('%Y/%m/%d %A %H:%M:%S')
            disp_data['date'] = dt_now
            
            return disp_data


# class RoundCreateView(CreateView):
#     model = Round
#     template_name = 'round_pages/list_golfhouse.html'
#     def get(self, request):
#         if "query_param" in request.GET:
#             # query_paramが指定されている場合の処理
#         param_value = request.GET.get("query_param")
#         else: