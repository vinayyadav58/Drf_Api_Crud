from django.urls import path
from.views import BookListAPI,CreateAPIView,BookRetriveAPI,BookDeleteAPIView,BookUpdateAPIView,upload_document,TokenObtainPairView,TokenRefreshSlidingView

urlpatterns = [
    path('',BookListAPI.as_view(),name='book_list'),
    path('books/create/',CreateAPIView.as_view(),name='book_create'),
    path('books/<int:book_id>/',BookRetriveAPI.as_view(),name='book_retrive'),
    path('books_delete/<int:book_id>/',BookDeleteAPIView.as_view(),name='book_delete'),
    path('books_update/<int:book_id>/',BookUpdateAPIView.as_view(),name='book_update'),
    path('document/upload/',upload_document,name='upload_doc'),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshSlidingView.as_view(),name='token_refresh'),
]