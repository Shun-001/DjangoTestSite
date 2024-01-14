from django.urls import path
from blogs.views import toppage, post_detail

urlpatterns = [
    path('', toppage),
    path('<slug:slug>/', post_detail, name='post_detail')
]
