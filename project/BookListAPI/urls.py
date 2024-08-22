from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
urlpatterns = [

    path('books/',view=views.books),
    path('menu-items/',view=views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>',view=views.SingleMenuItemView.as_view()),
    path('secret/',view=views.secret),
    path('manager-view/',view=views.manager_view),
    path('api-token-auth/',obtain_auth_token),
    path('throttle-check/',view=views.throttle_check),

]