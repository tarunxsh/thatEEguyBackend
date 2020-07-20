from django.shortcuts import render,redirect,get_object_or_404
from django.utils.text import slugify
from taggit.models import Tag
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from .forms import PostForm

# ===========================================================================================
# ARTICLE INDEX
# def index(request):
# 	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
# 	posts= Post.published.all()
# 	return render(request,'index.html',{'posts':posts})


# paginated article index
class ListIndex(ListView):
	model=Post 							#define one required model
	queryset = Post.published.all()
	context_object_name = 'posts'       #default context : {model}_list
	paginate_by = 5						#default context : page_obj
	template_name = 'index.html'


	#to add extra context vars using querysets
	def get_context_data(self, **kwargs):
		context = super(ListIndex,self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		print(context)
		return context


# ==========================================================================================
# List by tag
def ListByTag(request , tag_slug):
	alltags=Tag.objects.all()
	tag = get_object_or_404(Tag, slug=tag_slug)
	tagged_posts = Post.published.all().filter(tags__in=[tag])
	return render(request,'index.html',{'posts':tagged_posts,'tags':alltags})

# ===========================================================================================
# POST DETAIL
def post_detail(request,pk,slug):
	post = get_object_or_404(Post,pk=pk,slug=slug)
	return render(request,'post_detail.html', {'post':post})


# ==========================================================================================
# NEW POST 
@login_required
def newpost(request):
	#handling post request
	if request.method == 'POST':
		form = PostForm(request.POST) #PostForm instance with submitted data via post request
		if form.is_valid():
			cd=form.cleaned_data       #title and descp
			new_post = form.save(commit=False);
			new_post.author = request.user
			new_post.save()
			form.save_m2m()     #to save tags  //tags are many2many field 
			#modified save method of form to save author and slugify the title
			return redirect(new_post.get_absolute_url()) 

	else:
		form = PostForm()	
		return render(request,'newpost.html',{'form':form,'view':1})    
		# view:1 to show tags field in template




# ===========================================================================================
# POST EDIT
@login_required
def post_edit(request,pk):		
	if request.method == 'POST':
		edited_post = PostForm(request.POST)
		print(request.POST['title'])
		edited_slug=""
		if edited_post.is_valid():
			edited_title = request.POST['title']
			edited_descp =request.POST['descp']
			edited_slug = slugify(edited_title)
			print(edited_slug)
			Post.objects.filter(pk=pk).update(title=edited_title,descp=edited_descp,slug=edited_slug)
		return redirect('post_detail',pk=pk,slug=edited_slug)

		


	else:
		post = Post.objects.get(pk=pk)
		form = PostForm(instance=post)
		return render(request,'newpost.html',{'form':form, 'view':0})	
		# view:0 to not show tags field in template



# ===========================================================================================
# PUBLISH POST
@login_required
def post_publish(request, pk):
	post = Post.objects.get(pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk,slug=post.slug)


# ===========================================================================================
# DRAFT POST
@login_required
def post_draft(request,pk):
	post = Post.objects.get(pk=pk)
	post.draft()
	return redirect('post_detail', pk=pk,slug=post.slug)


# ===========================================================================================
# DRAFTS LIST
@login_required
def post_draft_list(request):
	author = request.user
	posts = Post.objects.filter(status='draft',author=author).order_by('-created_date')
	return render(request,'post_draft_list.html', {'posts':posts})
	

# ===========================================================================================
# DELETE POST
@login_required
def post_remove(request, pk,slug):
    post = Post.objects.get(pk=pk)
    post.delete()
    if slug=="drafts":
    	return redirect('post_draft_list')
    else:
    	return redirect('index')

# ===========================================================================================
# ABOUT PAGE
def about(request):
    return render(request, 'about.html')
