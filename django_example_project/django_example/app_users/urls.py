from django.urls import path
from app_users.views import MainLoginView, MainLogoutView

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('logout/', MainLogoutView.as_view(), name='logout'),
]