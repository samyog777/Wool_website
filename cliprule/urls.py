from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliprule/', views.ClipRuleList.as_view(), name='cliprule-list'),
]