import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
from utils.module_model import model_loader, image_classify, get_photo_path
from .main_path import PATH_FOLDER_MODEL, PATH_FOLDER_PROJECT
from .detete_all_files import delete_images, delete_image
model_path = (PATH_FOLDER_MODEL + "model_from_mentor.h5",
			  PATH_FOLDER_MODEL + "weights_from_mentor.h5")
model = model_loader(model_path)

def index(request):
	string = ''
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		#delete_images('./media/images')
		if form.is_valid():
			x = form.save()
			print(request.FILES['link'])
			full_name = "./media/images/" + str(request.FILES['link'])
			print(full_name)
			print(os.listdir('./media/images'))
			result = image_classify(full_name, 'si_rescale', model)
			delete_image(full_name)
			if round(result[0][2]*100, 2) < 50:
				string = ["We can", " understand "," what this image"," load another!"]
			else:
				string = ["This is the ", f"{result[0][1]}", " with chance ", f"{str(round(result[0][2]*100, 2))}%"]
	else:
		form = UserForm()
	return render(request, 'html/index.html', {'form': form, 'result': string})

def success(request):
	return HttpResponse('successfully uploaded')

	# news = Links.objects.all()
	# if request.method == "POST":
	# 	form = UserForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# print(f"\n\n {news[13]} \n\n")
	# save_photo(news[21])


	# form = UserForm()
	# data = {
	# 	'form': form,
	# 	'news': news
	# }
	# return render(request, 'html/index.html', data)
