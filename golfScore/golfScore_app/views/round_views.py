from django.db.models.query import QuerySet
from django.utils import dateformat,timezone
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,FormView
from golfScore_app.models import GolfHouseMaster,Round,CourseMaster,TeeingAreaMaster
from golfScore_app.forms import RoundCreateForm
# # Create your views here.
# def helloworld(request):
#     return HttpResponse('round Hello World!')
# def test(request):
#     return HttpResponse('round test')

today = datetime.datetime.today().date()

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


class RoundCreateView(FormView):
    template_name = 'round_pages/input_round.html'
    success_url = reverse_lazy('listGolfHouse')
    form_class = RoundCreateForm
    # def get_form_kwargs(self, *args, **kwargs):
    #     context = super(RoundCreateView, self).get_context_data(**kwargs)
    #     context["house_id"] = self.request.GET.get("pk")
    #     return context
    def get_form_kwargs(self):
        kwargs = super(RoundCreateView,self).get_form_kwargs()
        kwargs['house_id'] =self.kwargs['pk'] #service_idはパラメータ
        return kwargs

    def post(self, request, *args, **kwargs):
        # 選択されたゴルフ場のIDを取得
        house_id = self.kwargs['pk']
        
        # フォームで入力された値を取得
        # フォームの入力値を変数に設定
        play_date = request.POST['play_date']
        weather = request.POST['weather']
        wind = request.POST['wind']
        first_round = request.POST['first_round']
        second_round = request.POST['second_round']
        ex_round = request.POST['ex_round']
        teeing_area = request.POST['teeing_area']
        # ティーイングエリアを取得
        teeing_area_data = TeeingAreaMaster.objects.filter(teeing_area_id = teeing_area)[0]

        # ラウンドDBの基本データを設定
        round = Round(
            house_id = GolfHouseMaster.objects.get(pk = house_id),
            play_date = play_date,
            weather = weather,
            wind = wind,
            teeing_area = teeing_area_data.teeing_area_name
        )
        print(round)
        # 前半コースデータを取得
        if first_round and first_round != 0 :
            first_course_data = CourseMaster.objects.filter(house_id = house_id,course_id = first_round)[0]
            
            first_round = first_course_data.course_name
            round.hole_1 = first_course_data.hole_number_1
            round.hole_2 = first_course_data.hole_number_2
            round.hole_3 = first_course_data.hole_number_3
            round.hole_4 = first_course_data.hole_number_4
            round.hole_5 = first_course_data.hole_number_5
            round.hole_6 = first_course_data.hole_number_6
            round.hole_7 = first_course_data.hole_number_7
            round.hole_8 = first_course_data.hole_number_8
            round.hole_9 = first_course_data.hole_number_9
            # ハンディキャップ1-27
            round.handicap_1 = first_course_data.handicap_1
            round.handicap_2 = first_course_data.handicap_2
            round.handicap_3 = first_course_data.handicap_3
            round.handicap_4 = first_course_data.handicap_4
            round.handicap_5 = first_course_data.handicap_5
            round.handicap_6 = first_course_data.handicap_6
            round.handicap_7 = first_course_data.handicap_7
            round.handicap_8 = first_course_data.handicap_8
            round.handicap_9 = first_course_data.handicap_9
            # パー1-27
            round.par_1 = first_course_data.par_1
            round.par_2 = first_course_data.par_2
            round.par_3 = first_course_data.par_3
            round.par_4 = first_course_data.par_4
            round.par_5 = first_course_data.par_5
            round.par_6 = first_course_data.par_6
            round.par_7 = first_course_data.par_7
            round.par_8 = first_course_data.par_8
            round.par_9 = first_course_data.par_9
            
        # 後半コースデータの設定
        if second_round and second_round != 0 :
            second_round_data = CourseMaster.objects.filter(house_id = house_id,course_id = second_round)[0]
            
            round.second_round = second_round_data.course_name
            round.hole_10 = second_round_data.hole_number_1
            round.hole_11 = second_round_data.hole_number_2
            round.hole_12 = second_round_data.hole_number_3
            round.hole_13 = second_round_data.hole_number_4
            round.hole_14 = second_round_data.hole_number_5
            round.hole_15 = second_round_data.hole_number_6
            round.hole_16 = second_round_data.hole_number_7
            round.hole_17 = second_round_data.hole_number_8
            round.hole_18 = second_round_data.hole_number_9
            # ハンディキャップ1-27
            round.handicap_10 = second_round_data.handicap_1
            round.handicap_11 = second_round_data.handicap_2
            round.handicap_12 = second_round_data.handicap_3
            round.handicap_13 = second_round_data.handicap_4
            round.handicap_14 = second_round_data.handicap_5
            round.handicap_15 = second_round_data.handicap_6
            round.handicap_16 = second_round_data.handicap_7
            round.handicap_17 = second_round_data.handicap_8
            round.handicap_18 = second_round_data.handicap_9
            # パー1-27
            round.par_10 = second_round_data.par_1
            round.par_11 = second_round_data.par_2
            round.par_12 = second_round_data.par_3
            round.par_13 = second_round_data.par_4
            round.par_14 = second_round_data.par_5
            round.par_15 = second_round_data.par_6
            round.par_16 = second_round_data.par_7
            round.par_17 = second_round_data.par_8
            round.par_18 = second_round_data.par_9
            
        # 後半コースデータの設定
        if second_round and second_round != 0 :
            second_round_data = CourseMaster.objects.filter(house_id = house_id,course_id = second_round)[0]
            
            round.second_round = second_round_data.course_name
            round.hole_10 = second_round_data.hole_number_1
            round.hole_11 = second_round_data.hole_number_2
            round.hole_12 = second_round_data.hole_number_3
            round.hole_13 = second_round_data.hole_number_4
            round.hole_14 = second_round_data.hole_number_5
            round.hole_15 = second_round_data.hole_number_6
            round.hole_16 = second_round_data.hole_number_7
            round.hole_17 = second_round_data.hole_number_8
            round.hole_18 = second_round_data.hole_number_9
            # ハンディキャップ1-27
            round.handicap_10 = second_round_data.handicap_1
            round.handicap_11 = second_round_data.handicap_2
            round.handicap_12 = second_round_data.handicap_3
            round.handicap_13 = second_round_data.handicap_4
            round.handicap_14 = second_round_data.handicap_5
            round.handicap_15 = second_round_data.handicap_6
            round.handicap_16 = second_round_data.handicap_7
            round.handicap_17 = second_round_data.handicap_8
            round.handicap_18 = second_round_data.handicap_9
            # パー1-27
            round.par_10 = second_round_data.par_1
            round.par_11 = second_round_data.par_2
            round.par_12 = second_round_data.par_3
            round.par_13 = second_round_data.par_4
            round.par_14 = second_round_data.par_5
            round.par_15 = second_round_data.par_6
            round.par_16 = second_round_data.par_7
            round.par_17 = second_round_data.par_8
            round.par_18 = second_round_data.par_9
            
        
        round.save()
        return super().post(request, *args, **kwargs)
