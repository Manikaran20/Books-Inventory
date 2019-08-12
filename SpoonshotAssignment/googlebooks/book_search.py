import os
import requests
import json
from .models import Books

class my_dictionary(dict): 
  
    def __init__(self): 
        self = dict() 

    def add(self, key, value): 
        self[key] = value 

class gbooks():
    googleapikey=os.environ.get('API_KEY')  
    def __init__(self, book_search):
        self.book_search= book_search

    

    def search(self):       #Simple function to get the books detail which is to be shown to the users
        list1=[]
        list2=[]
        list3=[]
        idlist=[]
        list4=[]
        parms = {"q":self.book_search, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        my_json = r.json()
        for i in my_json["items"]:
            list1.append(i['volumeInfo']['title'])
            list2.append(i["volumeInfo"]["previewLink"])
            try:
                list3.append(i['volumeInfo']["imageLinks"]["thumbnail"])
            except:
                list3.append('#') #for the books which doesn't have a thumbnail
            idlist.append(i["id"])

        for j in idlist:        #checking which of the books are available in the store already
            if Books.objects.filter(ID= j):
                list4.append("available")
            else:
                list4.append("This item is not available in the inventory")

        data= zip(list1, list2, list3, list4)   
        return data

        
        
        
       