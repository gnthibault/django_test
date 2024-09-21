import debug_toolbar
from django.urls import path, include
from . import views


# This is a URLConf
urlpatterns = [
	path(
		route="hello/",
		view=views.say_hello
	),
	path('__debug__/', include(debug_toolbar.urls))
]
