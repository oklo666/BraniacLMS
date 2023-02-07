from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
<<<<<<< HEAD
=======

>>>>>>> main

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
<<<<<<< HEAD
    path("mainapp/", include("mainapp.urls", namespace="mainapp")),
=======
    path("mainapp/", include('mainapp.urls')),

>>>>>>> main
]
