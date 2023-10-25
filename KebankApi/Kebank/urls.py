from django.urls import path
from Kebank.Api.viewsets import *

urlpatterns = [
    path('legalperson/', LegalPersonViewSet.as_view({"get":"list"}) ),
    path('legalperson/', LegalPersonViewSet.as_view({"post":"create"}) ),
     path('usersteste/', LegalPersonViewSet.as_view({"post":"create"}) ),
]