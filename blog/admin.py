from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','created_date','status','author')
	prepopulated_fields = {'slug': ('title',)}
