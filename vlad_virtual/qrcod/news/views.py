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
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import News, Category, User1
from .forms import NewsForm, UserRegisterForm, UserLoginForm, AddNewsForm, QRform


def add_qr(request):

	# создание QR-кода

	if request.method == 'POST':

		form = QRform(request.POST)

		if form.is_valid():

			a = request.POST

			qr = qrcode.QRCode(
				version=3,
				error_correction=qrcode.constants.ERROR_CORRECT_L,
				box_size=20,
				border=2,
			)
			qr.add_data(a.get('content'))
			qr.make(fit=True)

			image = qr.make_image()

			os.remove('news/static/news/qrcode.jpg')

			image.save('news/static/news/qrcode.jpg')

			redirect('add_qr')
	else:
		form = QRform()


	return render(request, 'news/add_qr.html', {'form': form})


def user_logout(request):

	# деаутентификация пользователя

	os.remove('news/static/news/qrcode.jpg')

	logout(request)

	return redirect('login')


def user_login(request):

	# вход на сайт

	os.remove('news/static/news/qrcode.jpg')

	if request.method == 'POST':

		form = UserLoginForm(data=request.POST)

		if form.is_valid():

			user = form.get_user()
			login(request, user)

			return redirect('home')
	else:

		form = UserLoginForm()

	return render(request, 'news/login.html', {'form': form})


def register(request):

	# регистрация на сайте

	os.remove('news/static/news/qrcode.jpg')

	form = UserRegisterForm()

	if request.method == 'POST':

		form = UserRegisterForm(request.POST)

		if form.is_valid():

			user = form.save()
			login(request, user)
			messages.success(request, 'Вы успешно зарегистрировались')

			return redirect('home')
		else:

			messages.error(request, 'Ошибка регистрации')
	else:

		form = UserRegisterForm()

	return render(request, 'news/register.html', {"form": form})


def index(request):

	# стартовая страница с выводом всех мероприятий

	os.remove('news/static/news/qrcode.jpg')

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
	print(form)

	return render(request, 'news/add_news.html', {'form': form, 'news_item': news_item})


def add_news_form(request):

	# страница создания нового мероприятия

	if request.method == 'POST':
		form = AddNewsForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			return redirect('home_page')
	else:
		form = AddNewsForm()

	return render(request, 'news/add_news_form.html', {'form': form})


def qr(request, news_id2):

	# генерация и вывод qr кода для прохода на мероприятие

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
