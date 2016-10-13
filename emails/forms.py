from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

CHOICES=[('8','8'),
         ('4','4')]


class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
    time = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())