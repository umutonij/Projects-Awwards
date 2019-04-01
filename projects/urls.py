from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$', views.projects_today, name = 'projectsToday'),
    url(r'^search/', views.search_results, name='search_results'),
#     url(r'^new/project$', views.new_project, name='new-project')
]
