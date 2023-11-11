from django.db import models

class Links(models.Model):
	link = models.ImageField(upload_to='./images')

	# def __str__(self):
	# 	return self.link