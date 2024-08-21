from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [

    path('books/',view=views.books),
    path('menu-items/',view=views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>',view=views.SingleMenuItemView.as_view()),
    path('secret/',view=views.secret),
    path('api-token-auth/',obtain_auth_token),

]