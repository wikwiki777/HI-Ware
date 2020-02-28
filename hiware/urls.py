"""hiware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from accounts import urls as accounts_urls
from products import urls as products_urls
from products.views import index
from cart import urls as urls_cart
from checkout import urls as urls_checkout
# Only used in Dev
# https://docs.djangoproject.com/en/3.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include(products_urls)),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
