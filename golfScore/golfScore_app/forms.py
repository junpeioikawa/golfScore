from django import forms
from datetime import date
from .models import Round,CourseMaster,TeeingAreaMaster




class RoundCreateForm(forms.Form):
    # fields = ["house_id","play_date","weather","wind","first_round","second_round","ex_round","teeing_area","green"]
    play_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}),input_formats=['%Y-%m-%d'], initial=date.today,)
    weather = forms.fields.ChoiceField(
        choices = (
            ('1', '晴れ'),
            ('2', '曇り'),
            ('3', '雨'),
            ('4', '雪'),
        ),
        required=True,
        widget=forms.widgets.Select
    )
    wind = forms.fields.ChoiceField(
        choices=(
            ('1','なし'),
            ('2','微風'),
            ('3','弱'),
            ('4','中'),
            ('5','強'),
        )
        )
    first_round =forms.ChoiceField(
        widget=forms.widgets.Select
    )
    second_round = forms.ChoiceField(
        widget=forms.widgets.Select
    )
    ex_round = forms.ChoiceField(
        widget=forms.widgets.Select
    )
    teeing_area = forms.ChoiceField(
        widget=forms.widgets.Select
    )

    def __init__(self, *args, **kwargs):
        house_id = kwargs.pop('house_id')
        # super(RoundCreateForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        
        cours_list = CourseMaster.objects.filter(house_id = house_id)
        cours_choices = [(cours_data.course_id, cours_data.course_name) for cours_data in cours_list]
        self.fields['first_round'].choices = cours_choices
        self.fields['second_round'].choices = cours_choices
        self.fields['ex_round'].choices = cours_choices
        teeing_list = TeeingAreaMaster.objects.filter(house_id = house_id)
        teein_choices = [(teeing_data.teeing_area_id, teeing_data.teeing_area_name) for teeing_data in teeing_list]
        self.fields['teeing_area'].choices = teein_choices



        # self.fields['second_round'].queryset = cours_data
        # self.fields['ex_round'].queryset = cours_data
