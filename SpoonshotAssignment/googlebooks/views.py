from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from .models import Books
from .forms import SearchForm, UpdateForm, AddForm
from .book_search import gbooks
import re, json, requests
from django.utils import timezone
from .base_script import start1
import os


class IndexView(TemplateView):
	template_name='googlebooks/home.html'

	def get(self, request):
		search_form= SearchForm
		#start1()

		return render(request, self.template_name, {'searchform': search_form})

	def post(self, request):
		searchform= SearchForm(request.POST)
		if searchform.is_valid():
			volume= searchform.cleaned_data['search']
		a= gbooks(volume)
		b= a.search()
		try:
			if (b[0]==[]):
				return HttpResponse("No Books Found", status= 401)
		except:
			return render(request, 'googlebooks/search.html', {'b':b})

		




class InventoryView(ListView):
	model= Books
	template_name='googlebooks/inventory.html'
	

	def get(self, request):
		books=Books.objects.all()
		print (books)
		
		return render(request, self.template_name, {'books': books})

class BooksUpdate(TemplateView):
	def get(self, request, ID):
		form=UpdateForm
		return render(request, 'googlebooks/update.html', {'form':form})
	def post(self, request, ID):
		updateform= UpdateForm(request.POST)
		if updateform.is_valid():
			title=updateform.cleaned_data['title']
			preview_link=updateform.cleaned_data['previewLink']
			key=updateform.cleaned_data['ID']
			copies=updateform.cleaned_data['copies']

			q=Books.objects.filter(ID=ID)
			q.book_name=title
			q.preview_link=preview_link
			q.ID=key
			q.count=copies
			q.save()
		books= Books.objects.all()
		return render(request, 'googlebooks/inventory', {'books': books})


class BooksDelete(TemplateView):
	
	def get(self, request, ID):
		q=Books.objects.get(ID=ID)
		q.delete()
		books=Books.objects.all()
		return render(request, 'googlebooks/inventory.html', {'books': books})

class BooksAdd(TemplateView):
	def get(self, request):
		addform= AddForm
		return render(request, 'googlebooks/add.html', {'form':addform})

	def post(self, request):
		addform= AddForm(request.POST)
		if addform.is_valid():
			url=addform.cleaned_data['url']
			key=re.findall("id=.+?[&]", url)
			temp_key=key[0][3:-1]
		googleapikey=os.environ.get('API_KEY')
		book_url="https://www.googleapis.com/books/v1/volumes/{}".format(temp_key)
		r = requests.get(url=book_url, params={'key':googleapikey})
		my_json= r.json()
		p_link="https://books.google.co.in/books?id={}".format(temp_key)
		q=Books(book_name=my_json['volumeInfo']['title'], ID=temp_key, preview_link='p_link', created_at= timezone.now())
		q.save()
		books=Books.objects.all()
		return render(request, 'googlebooks/inventory.html', {'books':books})
