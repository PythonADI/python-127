"""
URL configuration for workshop_11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from core.views import (
    home_view,
    about_view,
    product_detail_view,
)
from users.views import (
    login_view,
    logout_view,
)
from social.views import (
    blog_view,
    friends_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('about-us/', about_view, name="about-us"),
    path('products/<slug:slug>/', product_detail_view, name='product_detail'),

    path('blog/', blog_view, name="test"),
    path('friends/', friends_view),
    
    path('login/', login_view),
    path('logout/', logout_view),
]
