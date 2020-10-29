#  Inventory 

A web portal implemented using Python/Django(MVT structure).

It contains the list of books in store and contains information about its copies and book info link provided by Google Book Api. Anybody can access it, there is no need to login or authenticate(for now).

** Features **
* User can add a book or also copy of a existing book to the bookstore.

  * remove or delete the book from the bookstore.

  * can also remove or delete the book from the bookstore.
  
  * A search box which shows the books with the help of Google Book Api for the given query.
  
  * Searched books have text on their bottom, weather it is already exist in bookstore or not.
  
 ** Assumptions **
 
  *Added some books with popular keywords to the inventory using Google book API with a script(base_script.py)
  
  * Delete and Edit options are only for the books that are in the inventory.
  
 ** Installation and Running the server **
 * Create a virtual environment.
 * git clone https://github.com/Manikaran20/Books-Inventory.git
 
** Install Requirements **
  * pip install -r requirements.txt
  * python3 manage.py makemigrations
  * python3 manage.py migrate
** Running the server **
 * python manage.py runserver
 your app will be running on  [locally here!](http://127.0.0.1:8000/)
    
 [Live app on heroku](https://limitless-ravine-32971.herokuapp.com/googlebooks/)
  

 
  
