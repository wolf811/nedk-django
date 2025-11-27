from django.urls import path
from . import views
# from .views import ProfileUpdateView, ProfileDetailView, UserRegisterView, UserLoginView, UserPasswordChangeView, UserForgotPasswordView,UserPasswordResetConfirmView, UserConfirmEmailView, EmailConfirmationSentView, EmailConfirmedView, EmailConfirmationFailedView, UserLogoutView, FeedbackCreateView
from .views import FeedbackCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('accreditation', views.accreditation, name='accreditation'),
    path('contacts', views.contacts, name='contacts'),
    # path('user/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    # path('user/<str:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name="logout"),
    # path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    # path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    # path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('register/', UserRegisterView.as_view(), name='register'),
    # path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    # path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    # path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    # path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
