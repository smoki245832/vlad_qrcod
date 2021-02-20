from django.shortcuts import render 

from news.models import News


def index(request):

	news = News.objects.order_by('-id')[0:5]

	return render(request, 'qrcod/index.html', {'news': news})
