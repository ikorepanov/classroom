from django import forms


class SeatsForm(forms.Form):
    variants = forms.IntegerField(label="Сколько вариантов?")
    rows = forms.IntegerField(label="Сколько рядов?")
    desks = forms.IntegerField(label="Сколько парт в ряду?")
    pupils_lst = forms.CharField(label="Ученики")
