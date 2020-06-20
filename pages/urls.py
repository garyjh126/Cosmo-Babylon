from django.urls import path, include
# from newsletter.api.views import JoinCreateAPIView

urlpatterns = [
    path('', include('contacts.urls'))
]
