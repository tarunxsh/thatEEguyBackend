from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):

	STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
	)


	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=250,unique_for_date='published_date',default="asdf")
	author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='blog_posts',null=True)
	descp = HTMLField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)        #not shown in admin / auto update
	published_date = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	

	class Meta:
		ordering = ('-published_date',)

	def publish(self):
		self.published_date=timezone.now()
		self.status = 'published'
		self.save()

	def draft(self):
		self.status = 'draft'
		self.save()
	

	def __str__(self):
		return self.title


	#cannonical url => base url
	def get_absolute_url(self):
		return reverse('post_detail',args=[self.pk ,self.slug])

	#The first manager declared in a model becomes the default manager. 
	objects = models.Manager() # The default manager.
	published = PublishedManager() # Our custom manager.