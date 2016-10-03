from django import forms

class EmailForms(forms.Form):
	content_data = forms.CharField(label=("data"), required=True,widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'data','rows': 3,}))