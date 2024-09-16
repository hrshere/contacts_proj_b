from django.urls import path
from .views import ContactListCreate, ContactDetail, MicrosoftAuthView, GoogleAuthView

urlpatterns = [
    path('contacts/', ContactListCreate.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('auth/microsoft/', MicrosoftAuthView.as_view(), name='microsoft_auth'),
    path('auth/google/', GoogleAuthView.as_view(), name='google-auth'),

]
