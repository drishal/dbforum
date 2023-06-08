from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *

def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
        # discussions.append(Discussion.objects.filter(forum_id=i.id))

    context={'forums':forums,
              'count':count,
              'discussions':discussions,
             }
    return render(request,'home.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html',context)

def addInDiscussion(request, forum_id):
    forum_instance = get_object_or_404(forum, id=forum_id)
    form = CreateInDiscussion(initial={'forum_id': forum_id})
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.forum_id = forum_id
            discussion.save()
            return redirect('/')
    context = {'form': form, 'forum': forum_instance}
    return render(request, 'addInDiscussion.html', context)


# def addInDiscussion(request, forum_id):
#     forum_instance = get_object_or_404(forum, pk=forum_id)
#     if request.method == 'POST':
#         form = CreateinDiscussion(request.POST)
#         if form.is_valid():
#             discussion = form.save(commit=False)
#             discussion.forum = forum_instance
#             discussion.save()
#             return redirect('home')
#     else:
#         form = CreateinDiscussion()
#     context = {'form': form, 'forum': forum_instance}
#     return render(request, 'addInDiscussion.html', context)

# def addInDiscussion(request, forum_id):
#     forum_instance = get_object_or_404(forum, id=forum_id)
#     form = CreateInDiscussion(initial={'forum_id': forum_id})
#     if request.method == 'POST':
#         form = CreateInDiscussion(request.POST)
#         if form.is_valid():
#             discussion = form.save(commit=False)
#             discussion.forum_id = forum_id
#             discussion.save()
#             return redirect('/')
#     context = {'form': form, 'forum': forum_instance}
#     return render(request, 'addInDiscussion.html', context)

# # def addInDiscussion(request, forum_id):
#     forum_instance = get_object_or_404(forum, id=forum_id)
#     form = CreateInDiscussion(initial={'forum': forum_instance})
#     if request.method == 'POST':
#         form = CreateInDiscussion(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form': form, 'forum': forum_instance}
#     return render(request, 'addInDiscussion.html', context)

# def addInDiscussion(request):
#     form = CreateInDiscussion()
#     if request.method == 'POST':
#         form = CreateInDiscussion(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context ={'form':form}
#     return render(request,'addInDiscussion.html',context)
