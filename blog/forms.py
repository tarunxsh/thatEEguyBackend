from django import forms
from django.utils.text import slugify
from .models import  Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','descp')
		widgets = {
			'title' : forms.TextInput(attrs={"placeholder":"Enter Title Here..."}),
		}

	def save(self,force_insert=False,force_update=False,commit=True):
		post = super().save(commit=False)
		post.slug=slugify(post.title)
		if commit:
			post.save()
		return post
