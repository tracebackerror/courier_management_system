from django.urls import path
from .views import *

urlpatterns = [
    path('', Shipping.as_view()),
    path('login/', Login.as_view()),
    path('register/',Register.as_view()),
    path('logout/',Logout.as_view()),
    path('tracking/',Tracking.as_view()),
    path('rate-calculator/',RateCalculator.as_view()),
]
