from django import forms

class SearchForm(forms.Form):
	search_string = forms.CharField(max_length=128, label="Vehicle name")
