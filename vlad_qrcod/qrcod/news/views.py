try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image, ImageDraw

import qrcode
import os

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.paginator import Paginator

from .models import News, Category, User
from .forms import NewsForm


def index(request):

	# стартовая страница с выводом всех мероприятий

	search_query = request.GET.get('q')

	if search_query:
		news = News.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
	else:
		news = News.objects.all()

	paginator = Paginator(news, 10)
	page_num = request.GET.get('page', 1)
	page = paginator.get_page(page_num)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
		'news': page,
		'title': 'Мероприятия Кванториума',
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
		}

	return render(request, 'news/index.html', context)


def get_category(request, category_id):

	# страница с выводом мероприятий из выбранной категории

	search_query = request.GET.get('q')

	if search_query:
		news = News.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query), category=category_id)
	else:
		news = News.objects.filter(category=category_id)

	paginator = Paginator(news, 10)
	page_num = request.GET.get('page', 1)
	page = paginator.get_page(page_num)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	category = Category.objects.get(pk=category_id)

	context = {
		'news': page,
		'title': category,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
		}

	return render(request, 'news/index.html', context)


def view_news(request, news_id):

	# страница с конкретной новостью 

	item = get_object_or_404(News, title=news_id)

	return render(request, 'news/view_news.html', {'item': item})


def add_news(request, news_id1):

	# страница регистрации нового пользователя

	news_item = get_object_or_404(News, title=news_id1)

	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.news = news_item
			a = 'qr/'
			x = a + str(news_id1)
			user.save()
			return redirect(x)
	else:
		form = NewsForm()

	form.news = news_item.title

	return render(request, 'news/add_news.html', {'form': form, 'news_item': news_item})


def qr(request, news_id2):

	# генерация и вывод qr кода 

	news = News.objects.get(title=news_id2)

	string = "http://127.0.0.1:8000/news/"

	stringx = string + str(news_id2)
	print(stringx)

	qr = qrcode.QRCode(
		version=3,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=20,
		border=2,
	)
	qr.add_data(stringx)
	qr.make(fit=True)

	image = qr.make_image()

	os.remove('news/static/news/qrcode.jpg')

	image.save('news/static/news/qrcode.jpg')


	return render(request, 'news/page.html', {'title': news.title, 'image': image, 'news': news})
