"""ideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin

from django.contrib.auth.views import LogoutView
from pages.views import HomeView, PageDetailView, contact_page
from accounts.views import LoginView, RegisterView #register_page, login_page,
from newsletter.api.views import JoinCreateAPIView

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout$', LogoutView.as_view(), name='logout'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^contact/$', contact_page, name='contact'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'api/email/join/$', JoinCreateAPIView.as_view(), name='email-join'),
    re_path(r'^(?P<slug>[\w-]+)/$', PageDetailView.as_view(), name='page-detail'),
]
