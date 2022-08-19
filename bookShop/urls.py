
from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from bookShop.views import  CreateNewReview, CreateNewBook, EditBook, EditReview, UserReview

# router = DefaultRouter()
# router.register('review', createNewView.as_view({'get' : 'list'}), basename='reviews')


urlpatterns = [
    path('list/', CreateNewBook.as_view(), name='new-book'),
    path('list/<int:pk>/', EditBook.as_view(), name='editbook'),
    path('review/', CreateNewReview.as_view(), name='review'),
    path('review/<int:pk>/', EditReview.as_view(), name='edit'),
    path('reviews/<str:username/', UserReview.as_view(), name='user-review')
]
# urlpatterns += router.urls
