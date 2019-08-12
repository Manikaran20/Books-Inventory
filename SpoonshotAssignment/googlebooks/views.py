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
# I have used CBV's to make it extensible


class IndexView(TemplateView): #The home view of the app
	template_name='googlebooks/home.html'

	def get(self, request):
		search_form= SearchForm
		#start1() #Just for the start of the app to store some books

		return render(request, self.template_name, {'searchform': search_form})

	def post(self, request):
		searchform= SearchForm(request.POST)
		if searchform.is_valid():
			volume= searchform.cleaned_data['search']
		a= gbooks(volume)
		b= a.search()
		
		
		return render(request, 'googlebooks/search.html', {'b':b})
		




class InventoryView(ListView): # The store view which will show the information about the store
	model= Books
	template_name='googlebooks/inventory.html'
	

	def get(self, request):
		books=Books.objects.all() #simply getting all the books in the store
		print (books)
		
		return render(request, self.template_name, {'books': books})

class BooksUpdate(TemplateView):
	def get(self, request, ID):
		form=UpdateForm
		return render(request, 'googlebooks/update.html', {'form':form})
	def post(self, request, ID):
		updateform= UpdateForm(request.POST)							#Because of the dependency of books on Google Book APi, Letting user update every field of the Books model
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
	
	def get(self, request, ID):		#Simply deleting a book and showing the updated list
		q=Books.objects.get(ID=ID)
		q.delete()
		books=Books.objects.all()
		return render(request, 'googlebooks/inventory.html', {'books': books})

class BooksAdd(TemplateView):
	def get(self, request):
		addform= AddForm
		return render(request, 'googlebooks/add.html', {'form':addform})

	def post(self, request): #To add a book, User just need to give the google book url, because I can't be dependent on user to provide me exact id of the google book
		addform= AddForm(request.POST)
		if addform.is_valid():
			url=addform.cleaned_data['url']
			key=re.findall("id=.+?[&]", url) #Getting the id from the url provided
			temp_key=key[0][3:-1]
		googleapikey= os.environ.get('API_KEY')
		book_url="https://www.googleapis.com/books/v1/volumes/{}".format(temp_key)# getting the book's information
		r = requests.get(url=book_url, params={'key':googleapikey})
		my_json= r.json()
		p_link="https://books.google.co.in/books?id={}".format(temp_key)
		q=Books(book_name=my_json['volumeInfo']['title'], ID=temp_key, preview_link='p_link', created_at= timezone.now())
		q.save()
		books=Books.objects.all()
		return render(request, 'googlebooks/inventory.html', {'books':books})
