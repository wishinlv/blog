"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_site import views
from django.urls import re_path

urlpatterns = [

    path('admin/', admin.site.urls),
]

# urlpatterns = [
#
#     path(r'', views.home),
#     path(r'about/', views.about),
#     path(r'contact/', views.contact),
#     re_path(r'^items/$', views.items),
#     re_path(r'^items/2018/$', views.archive_year),
#     re_path(r'^items/([201-201]{3}(2-8){1}/$', views.get_year)
#     path('blog/', views.blog),
#     re_path('blog/blog-page-([1-9]{1})/$', views.blog_page),
#     re_path('filter/', views.filter),
#     path('peoples/', views.people),
#     re_path('peoples/people-1', views.people_1),
#     re_path('peoples/people-2', views.people_2),
#     re_path('peoples/people-3', views.people_3)
#     path('form/', views.form),
#     re_path('Django_blog_dev/search/', views.search),
#     re_path('Django_blog_dev/save_to_file/', views.save_to_file),
#     re_path('Django_blog_dev/', views.html_form),
#     re_path('^db/', views.List.as_view()),
# path(r'', views.home),
# path('about/', views.about),
# path('contact/', views.contact),
# path('faq/', views.faq),
# path('how-it-works/', views.how_it_works),
# path('blog/', views.blog),
# re_path('blog/page-(\d+)/$', views.blog_page),
# re_path('form/', views.html_form),
# ]
