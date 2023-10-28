from django.urls import path
from Kebank.Api.viewsets import *

urlpatterns = [

    path('legalperson/', LegalPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('juridicperson/', JuridicPersonViewSet.as_view({"post":"create", "get":"list"})),
    path('account/', AccountViewSet.as_view({"post":"create", "get":"list"})),
    path("address/", AddressViewSet.as_view({"post":"create", "get":"list"})),
    path("card/", CardViewSet.as_view({"post":"create", "get":"list"})),
    path("loan/", LoanViewSet.as_view({"post":"create", "get":"list"})),
     path("card/<int:pk>", CardViewSet.as_view({"delete":"destroy", "get":"list"})),
    path("movimentation/", MovimentationViewSet.as_view({"get":"list"})),
]