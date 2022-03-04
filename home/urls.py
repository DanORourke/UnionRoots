from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<slug:slug>/', views.SimpleMarkdownView.as_view(), name='simple_markdown_view'),
]
