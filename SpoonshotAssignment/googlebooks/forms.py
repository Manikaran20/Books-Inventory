from django import forms
from .models import Books


class SearchForm(forms.Form):
	search= forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'search for a book'
		}
	)) 

class UpdateForm(forms.Form):
	title=forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Enter Title'
		}
	)) 
	previewLink=forms.URLField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Google books Link'
		}
	)) 
	ID= forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'must be google book id'
		}
	)) 
	copies=forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'how many copies you want to add'
		}
	)) 

class AddForm(forms.Form):
	url= forms.URLField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'url of the google book'
		}
	)) 
		
