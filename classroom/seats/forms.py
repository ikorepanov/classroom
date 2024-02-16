from django import forms

from .models import Arrangement, Seat, Student


# class SeatsForm(forms.Form):
#     variants = forms.IntegerField(label="Сколько вариантов?")
#     rows = forms.IntegerField(label="Сколько рядов?")
#     desks = forms.IntegerField(label="Сколько парт в ряду?")
#     pupils_lst = forms.CharField(label="Ученики")


class SomeForm(forms.Form):
    pupils_lst = forms.CharField(label="Ученики")


class ArrangementForm(forms.ModelForm):
    class Meta:
        model = Arrangement
        fields = ('month', 'year', 'columns', 'rows')
