from django import forms
from django.utils.text import slugify
from .models import  Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','descp' ,'tags')
		widgets = {
			'title' : forms.TextInput(attrs={"placeholder":"Enter Title Here..."}),
			'tags' : forms.TextInput(attrs={"placeholder":"tag1,tag2...."}),
		}

	def clean_tags(self):
		data = self.cleaned_data['tags']
		print(data)
		data=[i.lower() for i in data]
		print(data)
		return data



	def save(self,force_insert=False,force_update=False,commit=True):
		post = super().save(commit=False)
		post.slug=slugify(post.title)
		# post.tags = post.tags.lower()
		if commit:
			post.save()
		return post
