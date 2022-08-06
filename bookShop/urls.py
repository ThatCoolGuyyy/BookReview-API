from django.urls import path
from bookShop.views import CreateNewBook, CreateNewReview, EditBook, EditReview

urlpatterns = [
    path('list/', CreateNewBook.as_view(), name='new-book'),
    path('list/<int:pk>', EditBook.as_view(), name='editbook'),
    path('review/', CreateNewReview.as_view(), name='review'),
    path('review/<int:pk>', EditReview.as_view(), name='edit')
]
