from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from gestion import views

# fmt: off
urlpatterns = [
	path("", views.main, name="main"),
    path('tinymce/', include('tinymce.urls')),
	path("<int:order>/", views.unit, name="unit"),
	path("resource/<int:order>/", views.resource, name="resource")
]
# fmt: on

urlpatterns += staticfiles_urlpatterns()
