from django.urls import path
from Kebank.Api.viewsets import *

urlpatterns = [

    path('legalperson/', LegalPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('juridicperson/', JuridicPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('account/', AccountViewSet.as_view({"post":"create", "get":"list"})),
  
]