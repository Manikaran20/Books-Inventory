from rest_framework import routers
from googlebooks.api import BooksViewSet

router = routers.DefaultRouter()
router.register('googlebooks', BooksViewSet, 'googlebooks')
