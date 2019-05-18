from django.shortcuts import render
from django.http import HttpResponse
import os
import time
# Create your views here.

story_data = ""
started_time = time.time()
th_time = 1200
jeffery = ""
narayan = ""
rowlings = ""

def show(request):
	global story_data, started_time, th_time, jeffery, narayan, rowlings
	if (time.time() - started_time) > th_time:
		started_time = time.time()
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "w") as file:
			file.write("")

	context = {'data' : story_data, 'jeffery':jeffery, 'narayan':narayan, 'rowlings':rowlings}
	return render(request, 'Mainpage/home.php', context)

def execute(request):
	global story_data, started_time, th_time, jeffery, narayan, rowlings
	if (time.time() - started_time) > th_time:
		started_time = time.time()
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "w") as file:
			file.write("")
	
	if request.method == 'POST':
		form = request.POST
		generating_text = form.__getitem__('name')
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "a") as file:
			file.write(generating_text)
		command = str("python " + os.path.dirname(os.path.realpath(__file__)) + "/assets/predict.py")
		os.system(command)
	context = {'data' : story_data, 'jeffery':jeffery, 'narayan':narayan, 'rowlings':rowlings}
	return render(request, 'Mainpage/home.php', context)

def append(request):
	global story_data, started_time, th_time, jeffery, narayan, rowlings
	if (time.time() - started_time) > th_time:
		started_time = time.time()
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "w") as file:
			file.write("")
	if request.method == 'POST':
		form = request.POST
		try:	
			append_text = form.__getitem__('jeffery')
			final_text = ""
			with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/jeffery.txt"), "r") as file:
				final_text = file.read()

			with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "a") as file:
				file.write(" " + final_text)

		except:
			try:
				append_text = form.__getitem__('narayan')
				final_text = ""
				with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/narayan.txt"), "r") as file:
					final_text = file.read()

				with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "a") as file:
					file.write(" " + final_text)
			except:
				append_text = form.__getitem__('rowlings')
				final_text = ""
				with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/rowlings.txt"), "r") as file:
					final_text = file.read()

				with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "a") as file:
					file.write(" " + final_text)
		command = str("python " + os.path.dirname(os.path.realpath(__file__)) + "/assets/predict.py")
		os.system(command)
	context = {'data' : story_data, 'jeffery':jeffery, 'narayan':narayan, 'rowlings':rowlings}
	return render(request, 'Mainpage/home.php', context)

def generate(request):
	global started_time, th_time, jeffery, narayan, rowlings
	if (time.time() - started_time) > th_time:
		started_time = time.time()
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "w") as file:
			file.write("")
			
	if request.method == 'POST':
		form = request.POST
		predictions = form.__getitem__('predictions')
		with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/predictions.txt"), "w") as file:
			file.write(predictions)
	global story_data
	with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/story.txt"), "r") as file:
		story_data = file.read()
	with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/jeffery.txt"), "r") as file:
		jeffery = file.read()
	with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/narayan.txt"), "r") as file:
		narayan = file.read()
	with open(str(os.path.dirname(os.path.realpath(__file__))+"/static/upload/rowlings.txt"), "r") as file:
		rowlings = file.read()
	context = {'data' : story_data, 'jeffery':jeffery, 'narayan':narayan, 'rowlings':rowlings}
	return render(request, 'Mainpage/home.php', context)






