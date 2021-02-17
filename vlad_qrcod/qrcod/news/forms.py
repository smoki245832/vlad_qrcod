from django import forms 
from django.core.exceptions import ValidationError

from .models import User

import re


class NewsForm(forms.ModelForm):
	class Meta:
		model = User
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


'''class NewsForm(forms.Form):
	name = forms.CharField(max_length=150, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control',
	 'style': 'background-color: #F5F5F5;'}))
	last_name = forms.CharField(max_length=150, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control',
	 'style': 'background-color: #F5F5F5;'}))
	father_name = forms.CharField(max_length=150, label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control',
	 'style': 'background-color: #F5F5F5;'}))
	news = forms.ModelChoiceField(empty_label='Выберите Мероприятие', label='Мероприятие', 
		queryset=News.objects.filter(category='1'),
		widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #F5F5F5;'}))'''

