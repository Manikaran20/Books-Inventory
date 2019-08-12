from googlebooks.models import Books
from rest_framework import viewsets, permissions
from .serializers import BooksSerializer

# ScholarProfile Viewset

class BooksViewSet(viewsets.ModelViewSet):
	queryset = Books.objects.all()
	permission_classes = [
	permissions.AllowAny
	]
	serializer_class = BooksSerializer