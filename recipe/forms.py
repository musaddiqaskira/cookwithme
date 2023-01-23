from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label = '', widget= forms.TextInput
                           (attrs={'class':'search-bar',
				   'id':'', 'placeholder': 'Search Recipes, Authors, tags'}))

