from django import forms
from django.forms import ModelForm
from .models import Round,CourseMaster

class DateInput(forms.DateInput):
    input_type = 'date'


class RoundCreateForm(ModelForm):
    class Meta:
        model = Round
        fields = ["house_id","weather","wind","first_round","second_round","ex_round","teeing_area","green"]
        widgets = {
            'play_date': DateInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     house_id = kwargs.pop('house_id')
    #     super(RoundCreateForm, self).__init__(*args, **kwargs)
    #     cours_data = CourseMaster.objects.filter(house_id=house_id)
    #     self.fields['first_round'].queryset = cours_data
    #     self.fields['second_round'].queryset = cours_data
    #     self.fields['ex_round'].queryset = cours_data

