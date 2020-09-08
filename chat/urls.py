from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import MessagesView, SignUpView

app_name = 'chat'

urlpatterns = [
    path('', MessagesView.as_view(), name='index'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('acccount/logout/', LogoutView.as_view(next_page='chat:index'), name='logout'),
]
