from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('login/', user_login, name='login'),
	path('logout/', user_logout, name='logout'),
	path('register/', register, name='register'),
	path('', index, name='home'),
	path('category/<int:category_id>/', get_category, name='category'),
	path('<news_id>/', view_news, name='view_news'),
	path('add_news/<news_id1>', add_news, name='add_news'),
	path('add_news/qr/<news_id2>', qr, name='qr'),
]
