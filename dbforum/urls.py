from django.contrib import admin
from django.urls import path, include
from Discussion_Forum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',home,name='home'),
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]

