from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#def user_directory_path(instance, filename):
    ## file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return 'user_{0}/{1}'.format(instance.user.id, filename)

#def user_id(request, event= None):
#	global username
#	username = request.user.get_username()
#	return username

class files(models.Model):
	#user = models.CharField(max_length=100)
	file = models.FileField(upload_to = 'files/')
	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)