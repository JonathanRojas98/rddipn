from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from gestion import views

# fmt: off
urlpatterns = [
	path("", views.main, name="main"), 
	path("<int:order>/", views.unit, name="unit")
]
# fmt: on

urlpatterns += staticfiles_urlpatterns()
