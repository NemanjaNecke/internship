from django.urls import path, include
from rest_framework import routers
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from .views import AdminAccountCreateView, AdminAccountView, IpAddressView, ResendEmailVerificationView, UserAccountView, activate, CompanyViewSet, InvitationViewSet
from dj_rest_auth.views import PasswordResetConfirmView
from .views import InviteOnlyRegistrationView


router = routers.DefaultRouter()
router.register(r'invites', InvitationViewSet)

urlpatterns = [
    path(r'auth/ip-address', IpAddressView.as_view(), name='ip-address'),
    path(r'auth/register/admin/', AdminAccountCreateView.as_view(), name='create-company-admin'),
    path(r'auth/accounts/admin/', AdminAccountView.as_view(), name='admins'),
    path(r'auth/accounts/account/', UserAccountView.as_view(), name='account'),
    path('auth/register/<uidb64>/<token>', InviteOnlyRegistrationView.as_view(), name='register'),
    path(r'', include(router.urls)),
    path(r'companies/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='companies'),
     path(r'companies/<name>/deactivate', CompanyViewSet.as_view(
        {'get': 'retrieve', 'put': 'deactivate_company'}), name='companies_detail'),
    path(r'companies/<name>/activate', CompanyViewSet.as_view(
        {'get': 'retrieve', 'put': 'activate_company'}), name='companies_detail'),
    path(
        r'auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
        name='account_confirm_email'
    ),
    path(
        'auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path('auth/registration/resend-email/', ResendEmailVerificationView.as_view(),
         name="rest_resend_email"),
    path(r'auth/ip-address/activate-ip/<uidb64>/<token>', activate, name='activate-ip'),
    path(r'auth/', include('dj_rest_auth.urls')),
   
    path(
        'auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
]
