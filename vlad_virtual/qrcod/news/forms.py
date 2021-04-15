from django import forms 
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import User1, News

import re


class UserLoginForm(AuthenticationForm):

	# форма фхода

	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):

	# форма регистрации

	username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:

		model = User 
		fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):

	# форма участника формы

	class Meta:

		model = User1
		#fields = '__all__'
		fields = ['name', 'last_name', 'father_name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
			'father_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'})
		} 

	def clean_name(self):

		name = self.cleaned_data['name']
		
		if re.match(r'\d', name):
			raise ValidationError('Имя не должно начинаться с цифры')

		return name

	def clean_last_name(self):

		last_name = self.cleaned_data['last_name']
		if re.match(r'\d', last_name):
			raise ValidationError('Фамилия не должна начинаться с цифры')

		return last_name

	def clean_father_name(self):

		father_name = self.cleaned_data['father_name']
		if re.match(r'\d', father_name):
			raise ValidationError('Отчество не должно начинаться с цифры')

		return father_name


class AddNewsForm(forms.ModelForm):

	# форма участника формы

	class Meta:

		model = News
		#fields = '__all__'
		fields = ['title', 'content', 'created_at', 'updated_at']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
			'content': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
			'created_at': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
			'updated_at': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}),
		}
