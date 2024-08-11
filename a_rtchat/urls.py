from django.urls import path
from .views import *

urlpatterns = [
    path('', bagolyhuhogas_view, name="bagolyhuhogas"),

]