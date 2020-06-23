from . import views
from django.urls import  path


app_name = 'Blog'

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='index' ),
    path('<int:pk>/', views.BlogDetails.as_view(), name='details' ),
]
