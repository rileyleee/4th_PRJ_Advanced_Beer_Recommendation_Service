from django.urls import path
from community import views

app_name = 'community'
urlpatterns = [
    path('column/', views.columns),
    path('column/new/', views.column_new),
    path('column/<int:pk>/', views.column_detail),
    path("column/<int:pk>/edit/", views.column_edit),
    path('event/', views.events),
    path('event/new/', views.event_new),
    path('event/<int:pk>/', views.event_detail),
    path("event/<int:pk>/edit/", views.event_edit),
]

