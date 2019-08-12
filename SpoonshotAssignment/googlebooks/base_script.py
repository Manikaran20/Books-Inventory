import requests
import json
import os
from .models import Books
import random
from django.utils import timezone

def start1():
	Books.objects.all().delete()

	for i in ('love', 'dog', 'mother', 'friend', 'fake', 'value','zepplin'):
		googleapikey= os.environ.get('API_KEY')
		parms = {"q":i, 'key':googleapikey}
		r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
		my_json = r.json()
		list1=[]
		list2=[]
		list3=[]
		for i in my_json["items"]:
			list1.append(i['volumeInfo']['title'])
			list2.append(i['id'])
			list3.append(i["volumeInfo"]["previewLink"])

		for i, j, k in zip(list1, list2, list3):
			q= Books(book_name=i, ID=j, created_at= timezone.now(), preview_link=k, count= random.randint(0,20))
			q.save()
