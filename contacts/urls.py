from contacts import views
from django.urls import path
# from newsletter.api.views import JoinCreateAPIView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('ajax/validate_email/', views.validate_email, name='validate_email'),
    path('ajax/validate_form/', views.validate_form, name='validate_form'),
]
