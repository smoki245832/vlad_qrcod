from django.contrib import admin

from .models import News, Category, User1

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'content')
	list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	list_display_links = ('id', 'title')
	search_fields = ('title',)

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'last_name', 'news')
	list_display_links = ('id',)
	search_fields = ('name', 'last_name', 'news')
	list_filter = ('news',)



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User1, UserAdmin)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'
