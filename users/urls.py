from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from users.views import RegisterAccount, ConfirmAccount, LoginAccount, DetailsAccount

app_name = 'backend'

urlpatterns = [
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-confirm'),
    path('user/details', DetailsAccount.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
]