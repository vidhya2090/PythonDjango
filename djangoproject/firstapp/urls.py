
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.index.as_view(), name="index"),
    path('contact/', views.contact.as_view(), name="contact"),
    path('profile/', views.get_profile, name="profile"),
    path('form/', views.post_form, name="form"),
    path('edit_form/<int:pk>', views.edit_form, name="edit_form"),
    path('delete_form/<str:pk>', views.delete_form, name="delete_form"),
    path('records/', views.records.as_view(), name="records"),
]