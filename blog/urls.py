from django.urls import path,include
from .views import ListIndex,ListByTag, about,newpost,post_detail,post_publish , post_draft ,post_draft_list,post_remove,post_edit

urlpatterns = [
    # path('',index,name='index'),
    path('', ListIndex.as_view(), name='index'),
    path('tag/<slug:tag_slug>', ListByTag, name='list_by_tag'),
    path('about/', about ,name='about'),
    path('post/new', newpost ,name='newpost'),
    path('post/<int:pk>/<slug:slug>', post_detail, name='post_detail'),
    path('post/<pk>/publish/', post_publish, name='post_publish'),
    path('post/<pk>/draft/', post_draft, name='post_draft'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<pk>/remove/',post_remove, name='post_remove'),
    path('post/<pk>/edit/',post_edit, name='post_edit'),

]
