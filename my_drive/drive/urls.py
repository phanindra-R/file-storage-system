from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='drive-home'),
	path('about/',views.about, name='drive-about'),
	path('support/',views.support, name='drive-support'),
	path('help/',views.help, name='drive-help'),
	path('my_drive/', views.my_drive, name='my_drive'),
	path('uploads/', views.uploads, name='uploads'),
	path('files/<int:pk>/',views.delete_file, name='delete_file' ),
]